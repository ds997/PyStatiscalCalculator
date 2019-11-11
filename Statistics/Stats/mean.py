def mean(population_list):
    if len(population_list) == 0:
        return 0
    else:
        return sum(population_list) / float(len(population_list))
