from Statistics.Stats.mean import mean
from Statistics.Stats.standard_deviation import standard_deviation

def Pop_correlation_coefficient(population_list, population_list2):
    mean1, mean2 = mean(population_list), mean(population_list2)
    sd1, sd2 = standard_deviation(population_list), standard_deviation(population_list2)
    correlation = 0
    for i in range(0,len(population_list)):
        a = (population_list[i] - mean1)/sd1
        b = (population_list2[i] - mean2) / sd2
        correlation = correlation + (a * b)
    pop_correlation_coefficient = correlation / len(population_list)
    return pop_correlation_coefficient