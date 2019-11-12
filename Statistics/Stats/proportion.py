from Calculator.Division import division
from Calculator.Addition import addition


def proportion(population_list):
    t = 0

    for n in population_list:
        if (n % 2) == 0:
            t = addition(t, 1)
        result_proportion = division(t, len(population_list))
    return result_proportion