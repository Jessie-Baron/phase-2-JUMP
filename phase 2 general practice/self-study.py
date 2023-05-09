import statistics

list = [86, 125, 43, 54, 115, 92]
listB = [146, 132, 86, 125, 43, 54, 115, 92, 95, 116, 85, 124, 94, 142, 89]


def variance(data):
    # Number of observations
    n = len(data)
    # Mean of the data
    mean = sum(data) / n
    # Square deviations
    deviations = [(x - mean) ** 2 for x in data]
    # Variance
    variance = sum(deviations) / n
    return variance

print(statistics.variance(listB))

print(statistics.stdev(listB))

# print(sorted(listB))
