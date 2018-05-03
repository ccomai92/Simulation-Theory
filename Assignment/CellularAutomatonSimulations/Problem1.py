# 10.2 Project 9 
# Revise the function diffusion, which the section "Heat Diffusion" describes, 
# to be stochastic. Instead of multiplying each neighbor by r the rate of 
# diffusion, multiply each neighboring temperature by a different (1 + random_i)r,
# where random_i is a normally distributed random number with mean 0 and 
# std = 0.5. Adjust the coefficient of site so that the sum of all the 
# coefficients is 1. Run the model 100 times for 20 time steps and determine 
# the mean and range of temperatures for a designated cell towards the middle
# of the bar. 

import numpy as np
import matplotlib.pyplot as plt

AMBIENT_T = 25
HOT_T = 50
COLD_T = 10
D_RATE = 0.1

hotSites = [(0, 0), (0, 1)]
coldSites = [(4, 4), (4, 3)]

def initBar(m, n, hotSites, coldSites): 
    ambientBar = np.full((m, n), AMBIENT_T)
    return applyHotCold(ambientBar, hotSites, coldSites)
    
def applyHotCold(bar, hotSites, coldSites): 
    newBar = bar
    newBar[hotSites] = HOT_T
    newBar[coldSites] = COLD_T
    return newBar 
    
# N, Ne, E, SE, S, SW, W, NW are the temperature of the neighbor 
# site is the site (all grid) where temperature changes. 
def diffusion1(diffusionRate, site, N, NE, E, SE, S, SW, W, NW):
    return (1 - 8 * diffusionRate) * site \
            + diffusionRate * (N + NE + E + SE + S + SW + W + NW)

def diffusion2(diffusionRate, site, N, NE, E, SE, S, SW, W, NW): 
    randomR = (np.random.normal(0, 0.5, 8) + 1) * diffusionRate
    directions = np.array([N, NE, E, SE, S, SW, W, NW]) - site
    directions = directions * randomR
    return site + directions.sum()

def applyDiffusionExtended1(diffusionRate, barExtended):
    originBar = barExtended[1:-1, 1:-1]
    for y in np.arange(originBar[:,0].size) + 1:
        for x in np.arange(originBar[0,:].size) + 1:
            N = barExtended[x, y + 1]
            NE = barExtended[x + 1, y + 1]
            E = barExtended[x + 1, y]
            SE = barExtended[x + 1, y - 1]
            S = barExtended[x, y - 1]
            SW = barExtended[x - 1, y - 1]
            W = barExtended[x - 1, y]
            NW = barExtended[x - 1, y + 1]   
            site = barExtended[x, y]
            originBar[x - 1, y - 1] = diffusion1(diffusionRate,\
                                site, N, NE, E, SE, S, SW, W, NW)
    return originBar
    
def applyDiffusionExtended2(diffusionRate, barExtended):
    originBar = barExtended[1:-1, 1:-1]
    for y in np.arange(originBar[:,0].size) + 1:
        for x in np.arange(originBar[0,:].size) + 1:
            N = barExtended[x, y + 1]
            NE = barExtended[x + 1, y + 1]
            E = barExtended[x + 1, y]
            SE = barExtended[x + 1, y - 1]
            S = barExtended[x, y - 1]
            SW = barExtended[x - 1, y - 1]
            W = barExtended[x - 1, y]
            NW = barExtended[x - 1, y + 1]   
            site = barExtended[x, y]
            originBar[x - 1, y - 1] = diffusion2(diffusionRate,\
                                site, N, NE, E, SE, S, SW, W, NW)
    return originBar

# lat is grid 
# post: a grid extended on cell in each direction with reflecting 
#       boundary conditions was returned 
def reflectingLat(lat):
    firstRow = np.array([lat[0,:]]) 
    lastRow = np.array([lat[-1,:]])
    latNS = np.concatenate((firstRow, lat))
    latNS = np.concatenate((latNS, lastRow))
    firstCol = np.array([latNS[:,0]])
    lastCol = np.array([latNS[:,-1]])
    latNS = np.concatenate((firstCol.T, latNS), axis=1)
    latNS = np.concatenate((latNS, lastCol.T), axis=1)
    return latNS
    
def diffusionSim1(m, n, diffusionRate, t):
    bar = initBar(m, n, hotSites, coldSites)
    grids = np.array([bar])
    for i in np.arange(t): 
        barExtended = reflectingLat(bar)
        bar = applyDiffusionExtended1(D_RATE, barExtended)
        bar = applyHotCold(bar, hotSites, coldSites)
        barResult = np.array([bar])
        grids = np.append(grids, barResult, axis=0)
    return grids
    
def diffusionSim2(m, n, diffusionRate, t):
    bar = initBar(m, n, hotSites, coldSites)
    grids = np.array([bar])
    for i in np.arange(t): 
        barExtended = reflectingLat(bar)
        bar = applyDiffusionExtended2(D_RATE, barExtended)
        bar = applyHotCold(bar, hotSites, coldSites)
        barResult = np.array([bar])
        grids = np.append(grids, barResult, axis=0)
    return grids



grids1 = diffusionSim1(10, 10, D_RATE, 20)
grids2 = diffusionSim2(10, 10, D_RATE, 20)
nonStochasticSims = np.array([grids1])
stochasticSims = np.array([grids2])
for i in np.arange(99):
    grids1 = diffusionSim1(10, 10, D_RATE, 20)
    nonStochasticSims = np.append(nonStochasticSims, [grids1], axis=0)
    grids2 = diffusionSim2(10, 10, D_RATE, 20)
    stochasticSims = np.append(stochasticSims, [grids2], axis=0)
    
x1 = np.arange(20)
y1 = np.zeros(20) #nonstochastic mean

x2 = np.arange(20)
y2 = np.zeros(20)#stochastic mean

for i in np.arange(20):
    y1[i] =  nonStochasticSims[:, i, :, :].mean()
    y2[i] = stochasticSims[:, i, :, :].mean()
    
#print(nonStochasticSims)
#print(stochasticSims)
#print(nonStochasticSims.mean())
#print(stochasticSims.mean())

plt.plot(x1, y1, 'b', x2, y2, 'r')
plt.title("stochastic vs. deterministic")
plt.xlabel("time steps")
plt.ylabel("mean Temperature")
plt.show()
plt.savefig("Problem1.png")

