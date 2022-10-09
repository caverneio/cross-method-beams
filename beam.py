import itertools
import pandas as pd


class Beam:
    def __init__(self, sections):
        self.sections = sections

    def getNumberOfSections(self):
        return len(self.sections)

    def getSumOfDistributionFactors(self):
        return sum([1 / section.getLength() for section in self.sections])

    def getDistributionFactors(self):
        return (
            [0 if "l" in self.sections[0].getFixedEndSupports() else 1]
            + list(
                itertools.chain.from_iterable(
                    [
                        (1 / self.sections[section_index].getLength())
                        / (
                            (1 / self.sections[section_index].getLength())
                            + (1 / self.sections[section_index + 1].getLength())
                        ),
                        1
                        - (1 / self.sections[section_index].getLength())
                        / (
                            (1 / self.sections[section_index].getLength())
                            + (1 / self.sections[section_index + 1].getLength())
                        ),
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

    def getMoments(self, iterations=100):
        numberOfMoments = self.getNumberOfSections() - 1

        cross_table = self.runCrossMethod(iterations)

        moments = [round(cross_table.iloc[:, 0].sum(), 3)]
        for i in range(numberOfMoments):
            x = cross_table.iloc[:, i * 2 + 1].sum()
            moments.append(round(x, 3))

        moments.append(round(cross_table.iloc[:, -1].sum(), 3))

        return moments

    def getReactions(self):
        numberOfReactions = self.getNumberOfSections() + 1

        cross_table = self.runCrossMethod(4)

        reactions = []
        for i in range(numberOfReactions):
            x = cross_table.iloc[:, i * 2].sum()
            reactions.append(round(x, 3))

        return reactions
