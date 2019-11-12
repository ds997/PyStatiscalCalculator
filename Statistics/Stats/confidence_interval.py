from Statistics.Stats.standard_deviation import standard_deviation
from Statistics.Stats.mean import mean
from Calculator.Square_root import square_root


def confidence_interval(population_list):
    try:
        mean_var = mean(population_list)
        cin = 0.95
        value_of_z = (1 - cin) / 2
        stdev_var = standard_deviation(population_list)
        n = square_root(len(population_list))
        result = [mean_var - value_of_z * stdev_var / n, mean_var + value_of_z * stdev_var / n]
        return result
    except Exception as e:
        print("Error with Cintreval")
        return [0, 0]
