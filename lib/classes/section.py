from typing import List

from lib.classes.loads.load import Load


class Section:
    def __init__(self, length: float, loads: List[Load], fixedEndSupports: str = ""):
        self.length = length
        self.loads = loads
        self.fixedEndSupports = fixedEndSupports

    def __str__(self):
        return f"Length: {self.length} m, Load: {self.load} N/m, Reaction: {self.reaction} N, Moment: {self.moment} Nm"

    def getFixedEndMoments(self):
        return [
            sum([load.calcFixedEndMoments(self.length)[0] for load in self.loads]),
            sum([load.calcFixedEndMoments(self.length)[1] for load in self.loads]),
        ]

    def getMomentsByLoads(self):
        return sum([load.calcMomentByLoad(self.length) for load in self.loads])

    def getForcesByLoads(self):
        return sum([load.calcForceByLoad(self.length) for load in self.loads])

    def getLength(self):
        return self.length

    def getFixedEndSupports(self):
        return self.fixedEndSupports
