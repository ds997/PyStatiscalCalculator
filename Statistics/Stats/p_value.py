from scipy.stats import t


def P_value(population_list,confidence_level):
    degree_of_freedom = len(population_list) - 1
    alpha = (1 - confidence_level) / 2
    my_t = t.ppf(confidence_level, degree_of_freedom)
    my_p = 1 - t.cdf(my_t, degree_of_freedom)
    return my_p