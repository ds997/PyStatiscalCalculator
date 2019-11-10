from Statistics.Stats.mean import mean
from Statistics.Stats.median import median
from Statistics.Stats.mode import mode
from Statistics.Stats.standard_deviation import standard_deviation


class Statistics:
    result = 0

    def __init__(self):
        pass

    def mean(self, list):
        self.result = mean(list)
        return self.result

    def median(self, list):
        self.result = median(list)
        return self.result

    def mode(self, list):
        self.result = mode(list)
        return self.result

    def standard_deviation(self, list):
        self.result = standard_deviation(list)
        return self.result
