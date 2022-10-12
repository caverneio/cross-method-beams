from typing import List
import itertools
import pandas as pd

from lib.classes.section import Section


class Beam:
    def __init__(self, sections: List[Section]):
        self.sections = sections

    def __str__(self):
        return f"Beam: {self.sections}"

    def getNumberOfSections(self):
        return len(self.sections)

    def getSumOfDistributionFactors(self):
        return sum([1 / section.getLength() for section in self.sections])

    def getDistributionFactors(self):
        kl = lambda ind: (1 / self.sections[ind].getLength()) / (
            (1 / self.sections[ind].getLength())
            + (1 / self.sections[ind + 1].getLength())
        )

        return (
            [0 if "l" in self.sections[0].getFixedEndSupports() else 1]
            + list(
                itertools.chain.from_iterable(
                    [
                        kl(section_index),
                        1 - kl(section_index),
                    ]
                    for section_index in range(self.getNumberOfSections() - 1)
                )
            )
            + [0 if "r" in self.sections[-1].getFixedEndSupports() else 1]
        )

    def getFixedEndMoments(self):
        return list(
            itertools.chain.from_iterable(
                section.getFixedEndMoments() for section in self.sections
            )
        )

    def runCrossMethod(self, numberOfIterations=10):
        distributionFactors = self.getDistributionFactors()
        fixedEndMoments = self.getFixedEndMoments()

        cross_table = [fixedEndMoments]

        last_transported = fixedEndMoments

        for i in range(numberOfIterations):
            # Distribution
            distribution = []
            for index, item in enumerate(last_transported):
                if index == 0:
                    x = item * distributionFactors[0]
                    distribution.append(-x)
                elif index == len(last_transported) - 1:
                    x = item * distributionFactors[-1]
                    distribution.append(-x)
                elif index % 2 == 1:
                    x = (item + last_transported[index + 1]) * distributionFactors[
                        index
                    ]
                    distribution.append(-x)
                elif index % 2 == 0:
                    x = (last_transported[index - 1] + item) * distributionFactors[
                        index
                    ]
                    distribution.append(-x)

            cross_table.append(distribution)

            # Transport
            transport = []
            for t_index, t_value in enumerate(distribution):
                if t_index % 2 == 0:
                    x = distribution[t_index + 1]
                    transport.append(x * 0.5)
                elif t_index % 2 == 1:
                    x = distribution[t_index - 1]
                    transport.append(x * 0.5)

            cross_table.append(transport)

            last_transported = transport

        return pd.DataFrame(cross_table)

    def _getInternalMomentsCrossMethod(self, iterations):
        number_moments = self.getNumberOfSections() * 2

        cross_table = self.runCrossMethod(iterations)

        internal_moments = []
        for i in range(number_moments):
            x = cross_table.iloc[:, i].sum()
            internal_moments.append(round(x, 3))

        return internal_moments

    def getMoments(self, iterations=100):
        number_moments = self.getNumberOfSections() - 1

        internal_moments = self._getInternalMomentsCrossMethod(iterations)

        moments = [-internal_moments[0]]
        for i in range(number_moments):
            x = internal_moments[i * 2 + 1]
            moments.append(x)

        moments.append(internal_moments[-1])

        return moments

    def _getInternalReactions(self, iterations=100):
        internal_moments = self._getInternalMomentsCrossMethod(iterations)

        num_sections = self.getNumberOfSections()

        internal_reactions = []
        for i in range(num_sections):
            Rb = (
                -(
                    internal_moments[2 * i]
                    + internal_moments[2 * i + 1]
                    - self.sections[i].getMomentsByLoads()
                )
                / self.sections[i].getLength()
            )

            Ra = self.sections[i].getForcesByLoads() - Rb
            internal_reactions.append(Ra)
            internal_reactions.append(Rb)

        return internal_reactions

    def getReactions(self, iterations=100) -> List[float]:
        internal_reactions = self._getInternalReactions(iterations)
        reactions = [round(internal_reactions[0], 3)]
        for i in range(self.getNumberOfSections() - 1):
            x = internal_reactions[i * 2 + 1] + internal_reactions[i * 2 + 2]
            reactions.append(round(x, 3))

        reactions.append(round(internal_reactions[-1], 3))

        return reactions
