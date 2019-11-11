from Statistics.Stats.variance import variance


def standard_deviation(population_list):
    calculated_variance = variance(population_list)
    return calculated_variance ** 0.5
