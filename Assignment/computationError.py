import numpy as np
import matplotlib.pyplot as plt 

def investment(initial, year):
    for i in range(year):
       initial = initial + (initial * 0.093)
    return initial 
    
     
initial = 500  
years = np.array([10, 20, 30, 40]) # years
aResults = np.arange(4, dtype='d') # $ 
results = np.arange(4, dtype='d')  # $
aError = np.arange(4, dtype='d')   # $
rError = np.arange(4, dtype='d')   # %

for i in range(4): 
    aResults[i] = initial * np.exp(0.093 * (i + 1) * 10)
    results[i] = investment(initial, (i + 1) * 10)
    aError[i] = aResults[i] - results[i] 
    rError[i] = aError[i] / aResults[i] * 100

print('Absolute Error ($):', aError)
print('Relative Error (%):', rError)

plt.plot(years, aResults, 'rs--', years, results, 'bs--')
plt.title('Difference in Analytical and Computational calculation')
plt.xlabel('years')
plt.ylabel('investment value')
plt.show()
plt.savefig('ComputationalError.png')