# user adjustables 
# import os 
# path_inp = os.path.expanduser(os.path.join('~', work', 'obsdata', 'sheba', 'asfg', 'surf_temp'))
# '~/work/obsdata/sheba/asfg/surf_temp (in linux) 
# '~\\work\\obsdata (os specific)
# expnaduser add C:/user/Kris in front instead of ~ 
# path_out = os.curdir 
# if __name__ != "__main__": 
#   raise exception()
# try: 
#   ijday = float(idata_split[0])
# except: 
#   pass 
#
#
#   import numpy.ma as ma 
#   tempC = ma.masked_values([1, 2, 3, 4, -1e-10], -1e-10)
#   mask -1e-10 in the list, mask tell you which element is bad 
#   temC.filled() converts the masked array into array 
#   tempC.filled(-999) bad value become -999

#   import re (regular expressions)
#   'Lin, Asncion, Erdly'
#   'Lin,   Asuncion,Erdly' 
#   a = 'Lin, Erdly'.replace(" ", "")

# import pandas 
# prognostic: variable that evolves with time 
# diagnostic: variable no evolution of time 
# Probabilistic: model that either exhibits randomess or is driven by randomness 
# Deterministic: No randomness involved 
# Validation -> Meet requirements 
# Verification -> testing implementation 
# Weather -> Temperature 
#   verify: calibrate. verified model (existing data) -> makes sense in calculation
#           Data in the past 
#   Validate: model. whole series of numbers -> future prediction 
#               future: compare to prediction (Successfully predict future)
#           Data created over time 


# Specific issues: 
#   - Deterministic vs. Stochastic 
#   - Can we write an equation? 
#   - Simplifications? (What should I leave out?)
#   - Model runs/ Scenarios? 

# System Dynamics models: 
#   - "Global" vs. "Local" 
#   - "Aggregated" vs. "cellular automaton" 
#   -  "asdfdsfa" vs. "agent-based" (moving automaton)

# Discretization 
# 
# Algorithm 2 

numSim =  20
population = 100
growthR = 0.1
dTime = 0.005
growthRpS = growthR * dTime 
numIterations = (int) (numSim / dTime) 

for i in range(1, numIterations): 
    population += (population * growthRpS)
    t = i * dTime
    print("time ", t, "population ", population)
    
# analytical solution = not using computational power 