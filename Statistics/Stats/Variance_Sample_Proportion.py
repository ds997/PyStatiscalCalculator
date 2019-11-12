from Statistics.Stats.proportion import proportion
from Statistics.Stats.variance import variance


def variance_sample_proportion(numbers):
    variance_value = proportion(numbers)
    return variance(variance_value)

