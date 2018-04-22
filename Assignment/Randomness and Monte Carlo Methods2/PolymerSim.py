#! /usr/bin python3 
# S&S Module 14.1, Project 1:

import numpy as np 
import matplotlib.pyplot as plt 

# Project 1 
# a. develop a simulation and visulization to generate a 2D model 
#   of a polymer with a self-avoiding walk. Terminate the simulation
#    when the random direction would cause the developing path to cross itself. 
#    the visualizaiton should show the entire model of the polymer from the 
#    beginning of the random walk until the end. 

# pre: takes number of steps in the walk. 
# post: a list of points in the walk has been returned 
def check_history(x, y, history):
    for i in np.arange(int(history.size / 2)):
        xVal = history[(2 * i)]
        yVal = history[(2 * i) + 1]
        if (xVal == x and yVal == y):
            return False
    return True

def SAW_simulation(n = 100): 
    x = 0
    y = 0 
    history = np.array([x, y])
    count = 1
    while count <= n: 
        rand = np.random.randint(2)
        if rand == 0: 
            x += 1
        else: 
            x -= 1
        rand = np.random.randint(2)
        if (rand == 0): 
            y += 1 
        else: 
            y -= 1
        if check_history(x, y, history):
            history = np.append(history, x)
            history = np.append(history, y)
            count += 1
        else:
            return history
    return history
    
num_of_sim = 10
history = SAW_simulation(num_of_sim)
historyX = None
historyY = None
while history.size < 20: 
    history = SAW_simulation(num_of_sim)
    historyY = history[1::2]
    historyX = history[::2]

plt.figure(1)
plt.plot(historyX, historyY)
plt.show()
plt.title('Self_Avoid_Walk single simulation')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('single_sim.png')

# b and c 
#   Run the simulation a number of times, recording the fraction of times the
#   simulation generates a polymer of length (number of steps) at least n. 
#   Run the simulation a number of times, evaluating the root-mean-square 
#   displacement R_n 

def displacement_power2(x, y):
    return x**2 + y**2

num_of_sim = 50000
lengthN = 10
count = 0; 
fractions = np.zeros(num_of_sim, dtype='d')
successful = np.array([], dtype='d')
R_ns = np.array([], dtype='d')
for i in np.arange(1, num_of_sim): 
    history = SAW_simulation(lengthN * 2)
    if history.size > lengthN: 
        count += 1
        displacement = displacement_power2(history[-2], history[-1])
        successful = np.append(successful, displacement)
        R_ns = np.append(R_ns, np.sqrt(np.average(successful)))
    else: 
        pass 
    fractions[i] = count / i
    

plt.figure(2)
plt.plot(np.arange(num_of_sim - 1), fractions[1:])
plt.show()
plt.title('Fractions vs. number_of_trials')
plt.xlabel('Number_of_trials')
plt.ylabel('Fractions')
plt.savefig('f vs n.png')

plt.figure(3)
plt.plot(np.arange(R_ns.size - 1), R_ns[1:])
plt.show()
plt.title('Root_mean_square displacements')
plt.xlabel('number of successful trials')
plt.ylabel('Root_mean_square displacement')
plt.savefig('R_n vs n.png')


