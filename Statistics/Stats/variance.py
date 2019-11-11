from Statistics.Stats.mean import mean


def variance(population_list):
    result = 0
    result_mean = mean(population_list)
    for i in population_list:
        result += ((i - result_mean) ** 2)
    result_variance = result / len(population_list)
    return result_variance
