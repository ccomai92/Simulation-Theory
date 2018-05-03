# github.com/jwblin 
# Initbar 

AMBIENT_T = 25
HOT_T = 50
COLD_T = 10

import numpy as np

def initBar(m, n, hotSites, coldSites): 
    ambientBar = np.full((m, n), AMBIENT_T)
    return applyHotCold(ambientBar, hotSites, coldSites)
    
def applyHotCold(bar, hotSites, coldSites): 
    newBar = bar
    newBar[hotSites] = HOT_T
    newBar[coldSites] = COLD_T
    return newBar 
    