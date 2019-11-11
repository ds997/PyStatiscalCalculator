from Statistics.Stats.mean import mean
from Statistics.Stats.median import median
from Statistics.Stats.mode import mode
from Statistics.Stats.standard_deviation import standard_deviation
from Statistics.Stats.variance import variance
from Statistics.Stats.sample_mean import sample_mean
from Statistics.Stats.standardized_score import standardized_score
from Statistics.Stats.z_score import Z_score


class Statistics:
    result = 0

    def __init__(self):
        pass

    def mean(self, population_list):
        self.result = mean(population_list)
        return self.result

    def median(self, population_list):
        self.result = median(population_list)
        return self.result

    def mode(self, population_list):
        self.result = mode(population_list)
        return self.result

    def standard_deviation(self, population_list):
        self.result = standard_deviation(population_list)
        return self.result

    def variance(self, population_list):
        self.result = variance(population_list)
        return self.result

    def standardized_score(self, population_list):
         result_list = standardized_score(population_list)
         return result_list

    def sample_mean(self, population_list):
        self.result = sample_mean(population_list)
        return self.result
    def z_score(self, population_list):
         result_list = Z_score(population_list)
         return result_list
    '''
    def pop_correlation_coefficient(self, population_list):
         self.result = standard_deviation(population_list)
         return self.result
    '''