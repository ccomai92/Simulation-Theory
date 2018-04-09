# -*- coding: utf-8 -*-
"""
Module 2.1: System Dynamics Tool—Tutorial 1: Get the book's Python System 
Dynamics files, found here (Links to an external site.)Links to an external
site.. Once you've unzipped the folder, go to the sub-directory PythonSD 
Tutorials and go through the tutorial file, ProgrammingSDTutorial1.docx.
Do all questions, programs, and plots. For the last problem, entitled 
"Experimentation," the code file is OneCompartDilantin.py and is found 
in the PythonSDFiles sub-directory.  Any programming should be done in 
Python (including the plotting).
"""

import numpy as np
import matplotlib.pyplot as plt

# Quick Review Question1. 
#   Stock variables: aspirin_in_plasma 
#   Ordinary variables: half_life, plasma_volume, elimination-constant 
#   Derived stock variables: plasma_concentration
#   Flows: elimination 


################### Example: Drug Dosage (Single-Dose) ########################
#1. ordinary variables 
halfLife = 3.2          # hours 
plasmaVolume = 3000     # ml 

#2. elimination constant 
eliminationConstant = -np.log(0.5) / halfLife # /hours 

#3. 
initialAspirin = (float) (2 * 325 * 1000) 

#4. 
simulationHours = 8 #(hours)
deltaX = 5 / 60     #(minutes)
x = np.arange((1 / deltaX * simulationHours) + 1, dtype=np.float)
x = x * (deltaX)
aspirinInPlasma = np.zeros(x.size, dtype=np.float)
aspirinInPlasma[0] = initialAspirin

for i in range(1, x.size):
    elimination = (eliminationConstant * aspirinInPlasma[i - 1]) * deltaX
    aspirinInPlasma[i] = aspirinInPlasma[i - 1] - elimination 
    
plasmaConcentration = aspirinInPlasma / plasmaVolume

mtc = np.full(x.size, 350)
mec = np.full(x.size, 150)

plt.figure(0)
plt.plot(x, plasmaConcentration, color = 'g')
plt.plot(x, mtc, color = 'y')
plt.plot(x, mec, color = 'b')
plt.xticks(np.arange(0, 9, 2))
plt.yticks(np.arange(0, 501, 100))
plt.xlabel('hours')
plt.ylabel('plasma concentration (ug/ml)')
plt.title('Aspirin concentration over time')
plt.show()

# Quick Review Question2. 
#   a. 240 times 
#   b. 1, 2, 3, ..., 240 (inclusive)
#   c. 1, 2, 3, ..., 240 (inclusive)
#   d. i * 10 (minutes)
#   e. (i * 10) / 60 (hours)



################### Example: Drug Dosage (Repeated Doses) #####################

def xtoi(x): 
    return x / deltaX + 1
    
def itox(i): 
    return (i - 1) * deltaX


#1. ordinary variables 
mec = 10 
mtc = 20 
halfLife = 22 
volume = 3000 
dosage = 100 * 1000 
absorptionFraction = 0.12
interval = 8

#2. ordinary variables using defined ordinary variables
eliminationConstant = -np.log(0.5) / halfLife

#3. find initial value 
initialDrug = absorptionFraction * dosage 

#4. specifying total time and time increment, 
#   create vector of values from 0 through simulationHours 
#    with step size of deltaX
simulationHours = 168 
deltaX = 2 / 60
x = np.arange((1 / deltaX * simulationHours) + 1, dtype=np.float)
x = x * (deltaX)

drugInSystem = np.zeros(x.size, dtype=np.float)
drugInSystem[0] = initialDrug

for i in range(1, x.size):
    ingested = None
    if i != 1 and itox(i) % interval == 0: 
        ingested = absorptionFraction * dosage
    else: 
        ingested = 0 
    eliminated = (eliminationConstant * drugInSystem[i - 1]) * deltaX
    drugInSystem[i] = (drugInSystem[i - 1] + ingested - eliminated)

concentration = drugInSystem / volume
print(concentration.size)

mtc = np.full(x.size, 20)
mec = np.full(x.size, 10)

plt.figure(1)
plt.plot(x, concentration, 'g')
plt.plot(x, mtc, color = 'y')
plt.plot(x, mec, color = 'b')
plt.xticks(np.arange(0, 175, 50))
plt.yticks(np.arange(0, 27, 5))
plt.xlabel('hours')
plt.ylabel('concentration (ug/ml)')
plt.title('Dilantin concentration over time')
plt.show()
# Quick Review Question 3 
#    6 % 3 = 0 
#    7 % 3 = 1
#    8 % 3 = 2
#    9 % 3 = 0 

# Quick Review Question 4 
#    deltaX = 30 / 60 
#    interval = 12 
#    [25, 49, 73, 97, ...]

 