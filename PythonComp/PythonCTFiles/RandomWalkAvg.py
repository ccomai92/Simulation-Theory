# RandomWalkAvg.py
#
# 10.2  Random Walk 
#
# Introduction to Computational Science:  Modeling and Simulation for the Sciences
# Angela B. Shiflet and George W. Shiflet
# Wofford College
# Copyright 2006 by Princeton University Press
#
# Average over many runs to find average distance between first and last points
#

from math import sqrt
from random import randrange

def main():
    # determine points of path
    numTests = 100  # number of runs
    x0 = 0
    y0 = 0
    n = 25  # number of steps
    sumDist = 0   # sum of distances
    for j in range(numTests):
        x = x0
        y = y0
        for i in range(n):
            if randrange(2) == 0:
                x = x + 1
            else:
                x = x - 1
                
            if randrange(2) == 0:
                y = y + 1
            else:
                y = y - 1
        sumDist = sumDist + sqrt((x - x0)**2 + (y - y0)**2)

    print "Average distance between first and last points is", sumDist/numTests
 

main()
    
