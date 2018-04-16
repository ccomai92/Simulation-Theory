# Problem3. 

import math as m 
import numpy as np 
import matplotlib.pyplot as plt 
import random as r

# a. define the function f(x) = 2* pi sin(4 * pi * x)
def function(x): 
    result = (2 * m.pi) * np.sin(4 * m.pi * x) 
    return result 
    
# b. Plot f(x) from 0.0 to 0.25
xVals = np.arange(250, dtype='d')
xVals = xVals / 1000
yVals = np.zeros(250, dtype='d')
for i in np.arange(xVals.size): 
    yVals[i] = function(xVals[i])

plt.figure(1)
plt.plot(xVals, yVals)
plt.title('Probability_desity_function')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# c. assign to variable rand a uniform random number form 0.0 to 0.25
# and 
# d. 
def rej():
    randX = r.uniform(0.0, 0.25)
    randY = r.uniform(0, m.pi)
    if function(randX) > randY:
        return randX
    else: 
        return rej() 
        
#e. listX = np.arange(1000, dtype='d')
listY = np.zeros(1000, dtype='d')
for i in np.arange(listY.size): 
    listY[i] = rej(); 
    
plt.figure(1)
plt.hist(listY, 1000)
plt.title('Rejection Method')
plt.xlabel('Random Values')
plt.ylabel('Frequency')
plt.savefig('Problem3.png')
plt.show()