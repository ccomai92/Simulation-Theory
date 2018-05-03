#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=============================================================
#                 General Documentation

"""Single-function module. 
   See function docstring for description
"""

#-------------------------------------------------------------
#                 Additional Documentation 
# Notes:
# - Written for Python 3.5.2. 
# - See import statements throughout for more information
#   on non-built-in packages and modules required. 
#============================================================= 


#- Import Statements: 

from math import factorial 


#--------------- General Fuction: exponential ----------------

def exponential(x, tol = 1e-15): 
    """ Calculate exponential of Euler's number in open formula. 
    
    Method Arguments:
    * x: any types of scalar input
    * tol: specified absolute measure of precision after the 
            decimal point. Default tolerance is 1e-15. 
    
    Output: 
    * Exponential of x (e^x) in type of floating point. The
    result is calcuated within the precision of tolerance 
    given. 
        
    Reference: 
    *  “E (Mathematical Constant).” Wikipedia, Wikimedia 
            Foundation, 31 Mar. 2018, en.wikipedia.org/wiki/
            E_(mathematical_constant). 
    
    Examples with variable x and tol: 
       exponential(3.4, 1e-8)
       29.96410004404726
    """
    
    #- initializing variables 
    result = 0
    current = 1.0 # when n = 0, value is always 1.
    count = 1   # therefore, start counting from 1 
   
   #- Calculate current value and add to result
   #    until current value is smaller than the 
   #    given tolerance. 
    while tol < current: 
        result += current 
        current = (x**count) / factorial(count)
        print(current)
        count += 1 
        
    #- return exponential x of Euler's number (e^x) 
    return result
    
#- Execute test if moldue is run from command line: 
if __name__ == "__main__": 
    print("Output1: ", exponential(3.4), "\n")
    
    print("Output2: ", exponential(3.4, 1e-8), "\n")
    
    print("Output3: ", exponential(0.0003), "\n")
   
    print("Output4: ", exponential(0.0003, 1e-8), "\n")
  
    print("Output5: ", exponential(0.0003, 1e-3), "\n")
    
#========= end file =============