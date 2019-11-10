from Calculator.Statistics.mean import mean
from Statistics.Stats.standard_deviation import standard_deviation


def Standardised_score(my_population):
    mean_result = mean(my_population)
    stdev_result = standard_deviation(my_population)
    standardised_score = list()
    for x in my_population:
        my_score = (x - mean_result) / stdev_result
        standardised_score.append(my_score)
    return standardised_score
