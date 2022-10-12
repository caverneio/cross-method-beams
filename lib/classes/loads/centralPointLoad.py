from lib.classes.loads.load import Load


class CentralPointLoad(Load):
    def __init__(self, loadMagnitude):
        super().__init__(loadMagnitude)
        self.loadMagnitude = loadMagnitude

    def __str__(self):
        return f"{self.loadMagnitude} N"

    def calcFixedEndMoments(self, length):
        value = self.loadMagnitude * length / 8
        return [value, -value]

    def calcMomentByLoad(self, length):
        return self.loadMagnitude * length / 2

    def calcForceByLoad(self, length):
        return self.loadMagnitude
