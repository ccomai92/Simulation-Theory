# Problem1. 

import random as r
import numpy as np
import matplotlib.pyplot as plt


def function(x): 
    return (3 * x)
    
def area(xMin, yMin, xMax, yMax):
    return (xMax - xMin) * (yMax - yMin)
    
# xrange only from 0 to any positive integers 
def dart_simulation(num_of_darts, xMin, xMax):
    result = 0
    yMax = function(xMax)
    yMin = 0
    total_area = area(xMin, yMin, xMax, yMax)
    randomX = None
    randomY = None
    for i in range(num_of_darts):
        randomX = r.randint(xMin, xMax)
        randomY = r.randint(yMin, yMax)
        if randomY < function(randomX): 
            result = result + 1
    result = (total_area * (result / num_of_darts))
    return result

# from 0 to 1000 number of dart estimations 
estimations = np.zeros(500, dtype=object)

# each index holds the size of samples (i * 2)
for i in np.arange(estimations.size):
    estimations[i] = np.zeros(i * 2, dtype='d')

# run simulations for each sample size 
for i in np.arange(estimations.size):
    size = estimations[i].size
    for j in np.arange(size):
        estimations[i][j] = dart_simulation(100, 0, 2)

# find standard deviations for each samples 
stds = np.zeros(estimations.size)
for i in range(stds.size): 
    stds[i] = np.std(estimations[i])

x = np.arange(estimations.size)
x = x * 2
plt.plot(x, stds)
plt.title('Changes in std with respect to the sample size')
plt.xlabel('The number of samples')
plt.ylabel('Standard Deviations')
plt.savefig('changes_in_std.png')
plt.show()