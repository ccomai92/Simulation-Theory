# Develop a fire simulation in which every cell in a 17 * 17 grid has a
# tree and only the middle cell's tree is on fire initially. Do not 
# consider the possibility of lightning or tree growth. The simulation
# should have a parameter for burnProbability, which is the probability
# that a tree adjacent to a burning tree catches fire. The function 
# should return the percent of the forest burned. The program should run 
# eight experiments with burn probability = 10% 20% 30% and 90% and 
# should conduct each experiement 10 times. Also have the code determine 
# the average percent burned for each probability. Plot the data and fit
# a curve to the data. Discuss the results 

import numpy as np 
import matplotlib.pyplot as plt 
from random import random
EMPTY = 0
TREE = 1
BURNING = 2

def initForest(n, probBurning):
    probTree =  0.5    # probability of grid site occupied by tree
                       # (value 1); i.e., tree density
      # probability that a tree is burning (value 2);
                       # i.e., fraction of burning trees

    forest = np.zeros(n * n, dtype='int').reshape(n, n)

    for i in range(n):
        for j in range(n):
            if random() < probTree:
                if random() < probBurning:
                    forest[j, i] = BURNING
                else:
                    forest[j, i] = TREE
            else:
                forest[j, i] = EMPTY   

    return forest
    
def extendLat(lat):
    firstRow = np.array([lat[0,:]]) 
    lastRow = np.array([lat[-1,:]])
    latNS = np.concatenate((lastRow, lat))
    latNS = np.concatenate((latNS, firstRow))
    firstCol = np.array([latNS[:,0]])
    lastCol = np.array([latNS[:,-1]])
    latNS = np.concatenate((lastCol.T, latNS), axis=1)
    latNS = np.concatenate((latNS, firstCol.T), axis=1)
    return latNS
    
def spread(site, N, E, S, W):
    probImmune = 0.5     # probability of immunity from catching fire - global variable
    if (site == EMPTY) or (site == BURNING):
        returnValue = EMPTY
    elif (site == TREE) and ((N == BURNING) or (E == BURNING) or
                             (S == BURNING) or (W == BURNING)):
        if random() < probImmune:
            returnValue = TREE
        else:
            returnValue = BURNING
    else:
        returnValue = TREE

    return returnValue
    
def applyExtended(forestExtended):
    forest = forestExtended[1:-1, 1:-1]
    for y in np.arange(forest[:,0].size) + 1:
        for x in np.arange(forest[0,:].size) + 1:
            N = forestExtended[x, y + 1]
            E = forestExtended[x + 1, y]
            S = forestExtended[x, y - 1]
            W = forestExtended[x - 1, y]
            site = forestExtended[x, y]
            forest[x - 1, y - 1] = spread(site, N, E, S, W)
    return forest
            
def simulation(t, probBurning): 
    forest = initForest(t, probBurning)
    grids = np.array([forest])
    for i in np.arange(t): 
        forestExtended = extendLat(forest)
        forest = applyExtended(forestExtended)
        grids = np.append(grids, [forest], axis=0)
    return grids
    
probBurning = np.arange(1, 10) / 10
result = np.zeros(9)
for i in np.arange(probBurning.size): 
    resultTemp = np.zeros(10)
    for j in np.arange(probBurning.size + 1):
        grids = simulation(10, probBurning[i])
        first = grids[0,:,:]
        last = grids[-1,:,:]
        temp = first - last
        burnedTree= temp[np.where(temp > 0)].size
        resultTemp[j] = burnedTree
    result[i] = np.mean(resultTemp)

x = np.arange(result.size) / 10
result = result / 289 * 100
plt.figure(1)
plt.scatter(x, result)
# something for curvefit
plt.show()
plt.title("Average percent burned with respect to the burning probability")
plt.xlabel("burning probability")
plt.ylabel("average percent burned")
plt.savefig("Problem2.png")