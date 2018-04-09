#!/usr/bin/env python3
#===============================================================
#                       General Documentation 
"""Single-function module. 
   See function docstring for description
""" 

#--------------------------------------------------------------
#                   Additional Documentation 
# Notes: 
# - Written for Python 3.5.2.
# - See import statements throughout for more information on 
#   non-built-in packages and modules required 
#==============================================================


#------------------ General Function: Distance -----------------

#- Import statements: 
import numpy as N
from math import sqrt 


def distance(x, y, point):
    """Calculate distance. 
    
    Method Arguments: 
    * x: array defined in the NumPy package that contains
        integer values which represent x-locations in the
        Cartesian grid.
    * y: array defined in the NumPy package that contains
        integer values which represent y-locations in the
        Cartesian grid.
    * point: array defined in the NumPy package that contains
            two floating point or integer values which represent
            x and y coordiantes respectively. 
        
    Output: 
    * Return a NumPy array in shape of Cartesian grid defined by 
      given x and y coordiates which holds the distances from given
      point to each location on the grid. 
        
    Examples with x, y and point values: 
        import numpy as N 
        x = N.array([-2, -1, 0, 1, 2])
        y = N.array([-2, -1, 0, 1, 2]) 
        in this case, (0, 0) is in the middle
        pt = N.array([0, 0]) 
        print(distance(x, y, pt))
        [[ 2.82842712  2.23606798  2.          2.23606798  2.82842712]
         [ 2.23606798  1.41421356  1.          1.41421356  2.23606798]
         [ 2.          1.          0.          1.          2.        ]
         [ 2.23606798  1.41421356  1.          1.41421356  2.23606798]
         [ 2.82842712  2.23606798  2.          2.23606798  2.82842712]]
    """
    
    #- make Cartesian grid in size of x * y that contains
    #   double-precision floating-point numbers and initialize
    #   each value equal to zero. 
    
    result = N.zeros((N.size(y), N.size(x)), dtype = 'd')
    
    #- Calculate distance from the given point to each coordinate
    #   in the Cartesian grid. 
    for i in range(N.size(y)): 
        for j in range(N.size(x)): 
            result[i, j] = \
            sqrt((x[j] - point[0])**2 + (y[i] - point[1])**2)
    
    #- Return Cartesian grid containing distances from the given 
    #    point: 
    return result 

#- Execute test if module is run from command line: 

if __name__ == "__main__": 
    x = N.array([-2, -1, 0, 1, 2])
    y = N.array([-2, -1, 0, 1, 2]) 
    pt = N.array([0, 0]) 
    print("output1: \n", distance(x, y, pt), "\n")

    x = N.array([0, 1, 2, 3, 4])
    y = N.array([0, 1, 2, 3])
    pt = N.array([-2.3, 3.3])
    print("output2: \n", distance(x, y, pt), "\n")
    
    x = N.array([-4, -3, -2, -1, 0])
    y = N.array([-3, -2, -1, 0])
    pt = N.array([0, 0])
    print("output3: \n", distance(x, y, pt), "\n")
    
# ========================== end file ================================
