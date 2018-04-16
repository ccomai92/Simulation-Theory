# Problem 2. 
# Box-Muller-Gauss Methods for Normal Distribution with 
# Mean and Standard deviation. 
#   Compute b * sin(a) + mean and b * cos(a) + mean where 
#    a = a uniform random number in [0, 2pi)
#    rand = a uniform random number in [0, 1)
#    b = std * sqrt(-2 ln(rand))

import random as r 
import numpy as np
import math as m
import matplotlib.pyplot as plt 

def BMG_method(std=2, mean=9): 
# a. Assign go a a uniformly distributed random number between 0 and 2pi 
    a = r.uniform(0, 2 * m.pi)
 
# b. Assign b with stdDev = 2
    rand = r.uniform(0, 1)
    b = std * np.sqrt(-2 * np.log(rand))

# c. find x and y 
    x = b * np.cos(a) + mean 
    y = b * np.sin(a) + mean
    
    result = [x, y]
    return result 
    

# d. 
tblGauss = np.zeros((500, 2), dtype='d')

for i in np.arange(500): 
    result = BMG_method()
    tblGauss[i, 0] = result[0]
    tblGauss[i, 1] = result[1]
    
tblGauss = tblGauss.flatten()

# e. display histo gram of tblGauss 
plt.hist(tblGauss, 100)
plt.title('Box-Muller-Gauss Methods: mean = 9, std = 2')
plt.xlabel('Random Values')
plt.ylabel('Frequency') 
plt.grid(True)
plt.savefig('Problem2_e.png')
plt.show()

# f. no built in method so no g