from Statistics.Stats.mean import mean


class Statistics:
    result = 0

    def __init__(self):
        pass

    def mean_(self, list):
        self.result = mean(list)
        return self.result
