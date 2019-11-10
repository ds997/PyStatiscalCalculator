from Statistics.Stats.mean import mean
def Variance(list):
    sum = 0
    my_mean = mean(list)
    for i in list:
        sum += ((i - my_mean) ** 2)
    my_variance = sum/len(list)
    return my_variance
