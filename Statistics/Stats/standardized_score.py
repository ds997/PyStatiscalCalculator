from Calculator.Statistics.mean import mean
from Statistics.Stats.standard_deviation import standard_deviation

def Standardised_score(my_population):
    my_mean = mean(my_population)
    my_sd = standard_deviation(my_population)
    standardised_score = list()
    for x in my_population:
        my_score = (x - my_mean) / my_sd
        standardised_score.append(my_score)
    return standardised_score