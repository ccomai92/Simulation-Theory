import numpy as np
a = 44
def foo(*args, **kwds): # (positional, keyword) input parameters
    x = args[0]
    y = args[1]
    tol = kwds['tol']
    foo = kwds['foo'] 
    return x * y * tol * foo 
    
print(__name__)
if __name__ == "__main__": 
    if foo(4, 3, tol = 1, foo = 1) != 12: 
        raise ValueError("no!!!") 
    else: 
        print("success!") 

con = np.logical_and(a >=1, a<=3) 
np.where(a>2, -999, a * 2) 
np.where(np.logical_and(a >= 1, a <=3), 444, -1) 
np.logical_not(con) * (-1) 
con * 444 + np.logical_not(con) * (-1) 