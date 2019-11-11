
def mode(population_list):
    size = len(population_list)
    data = []
    for i in range(0, size, 1):
        data.append(population_list.count(population_list[i]))
    m = max(data)
    for x in population_list:
        if population_list.count(x) == m:
            return x
