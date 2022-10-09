from load import Load


class DistributedLoad(Load):
    def __init__(self, loadMagnitude):
        super().__init__(loadMagnitude)
        self.loadMagnitude = loadMagnitude

    def __str__(self):
        return f"{self.loadMagnitude} N/m"

    def calcFixedEndMoments(self, length):
        value = self.loadMagnitude * length**2 / 12
        return [-value, value]
