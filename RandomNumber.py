# Random Number 
#   Non-Causal, Non-deterministic 
#   
# Pseudorandom Number 
#   looks like random value 
#   repeating period occurs, goes long enough sequnce 
#       repeats
#   
# Generating Random Numbers 
#   - Multiplicative Linear Congruential Method (MLCM)
#   

import numpy as np

def RNGenerator(max): 
    result = []
    seed = 10
    multiplier = 2
    increment = 5
    modulus = max + 1
    for i in range(2 * max):
        next = (multiplier * seed + increment) % modulus
        result.append(next)
        seed = next
    return result
    
def RFGenerator(max):
    list = RNGenerator(max)
    list = np.array(list)
    list = list / (max + 1)
    return list
print(RNGenerator(10))
print(RFGenerator(10))

def my_int_random(n, seed=3382, modulus=42365):
    increment = 0; 
    multiplier = 16807
    r = np.zeros(n, dtype='l')
    r[0] = seed 
    for i in range(1, np.size(r)):
        r[i] = (multiplier * r[i-1] + increment) % modulus
    return r 
    
def my_uniform_random(n, seed=3382, modulus=42365):
    r = my_int_random(n, 3382, 42365)
    r = r / modulus
    return r
    
# Random 
#   Mersenne Twister 
#   2^19937 - 1
#   import random 
#   random() -> random point value btw [0, 1)
#   randint(a, b) [a, b]
#   seed 
#   uniform(a, b) return [a, b)
#   

import random as r
"""for i in range(10): 
    r = r.random()
    if r < 0.5: 
        print("heads")
    else: 
        print("tails") """
        

def dice_rolling():
    return r.randint(1, 6)
sum = 0
history = {}
for i in range(1000):
    diceVal1 = dice_rolling()
    diceVal2 = dice_rolling()
    sum = diceVal1 + diceVal2 
    #history[sum] = history[sum] + 1

print(sum)
print(history)    


# Monte Carlo Simulation 
# 

# Non-uniformly distributed Random Values 
#   probability : chance event occur 
#   Random Value: value is determined probabilistically 
#   Discrete probability: RV will speciffically = a value 
#   Continuous distribution: 
#       infinite values of possiblities so probability is 0 
#       still able to measure range 
#   
#   uniform -> non-uniform (by transforming it)
#       Discrete: if  
#       Normal : Box-Mueller-Gauss
#       Exp: Natural log 
#       Any: Rejection method

# Uniform probability is straight line 

# Rejection function 
#   