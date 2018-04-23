#=============================================================================
# Rejection method for arbitrary distribution:  Sine distribution
#
# Solution to Shiflet & Shiflet (2014)'s Quick Review Question 10 (p. 400)
# distribution.
#
# By Johnny Lin
# April 18, 2015
#
# Notes:
# - About adjusting multi-panel spacing:
#   http://stackoverflow.com/questions/6541123/improve-subplot-size-spacing-
#   with-many-subplots-in-matplotlib
# - About sub-panels:
#   http://matplotlib.org/users/pyplot_tutorial.html
# - About the tight_layout function:
#   http://matplotlib.org/api/tight_layout_api.html
# - The matplotlib subplot command increments through rows first:
#   http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.subplot
# - About the rejection method:
#   http://www.wikicoursenote.com/w/
#   index.php?title=Acceptance-Rejection_Sampling&oldid=475
#=============================================================================


#========================== USER ADJUSTABLE (begin) ==========================
N_PTS = 100000 #- number random points
n_bins = 60    #- number bins for the histogram
#=========================== USER ADJUSTABLE (end) ===========================


import numpy as N
import matplotlib.pyplot as plt


def f(x):
    return 2.0*N.pi * N.sin(4.0*N.pi*x)


#- Solution using looping:

def looping_solution():
    output = N.zeros(N_PTS)
    i = 0
    while i < N_PTS:
        randInterval = N.random.uniform(low=0.0, high=0.25)
        randUpperBound = N.random.uniform(low=0.0, high=2.0*N.pi)
        if f(randInterval) > randUpperBound:
            output[i] = randInterval
            i = i + 1

    return output


#- Solution using NumPy:

def numpy_solution():
    output = N.zeros((0,))
    output_length = N.size(output)

    while output_length < N_PTS:
        randInterval = N.random.uniform(low=0.0, high=0.25, size=(N_PTS,))
        randUpperBound = N.random.uniform(low=0.0, high=2.0*N.pi, size=(N_PTS,))

        temp = randInterval[N.where( f(randInterval) > randUpperBound)]
        output = N.concatenate([output, temp])
        output = output[0:N_PTS]
        output_length = N.size(output)

    return output


#- Plotting:

import time
a = time.time()
for i in range(10):
    samples1 = looping_solution()
print("Loops: " + str(time.time() - a))

import time
a = time.time()
for i in range(10):
    samples2 = numpy_solution()
print("NumPy: " + str(time.time() - a))

plot_range = N.array([0.0, 0.25])    #- range for plot x-axis

plt.figure(1)
plt.subplot(2,1,1)  #- numrow, numcols, fignum
plt.hist(samples1, bins=n_bins, align="mid", range=plot_range, color='r')
plt.title("Rejection Method Using Looping")
plt.ylabel("Count")

plt.subplot(2,1,2)
plt.hist(samples2, bins=n_bins, align="mid", range=plot_range, color='b')
plt.title("Rejection Method Using NumPy")
plt.xlabel("Random Variable")
plt.ylabel("Count")

plt.tight_layout()
plt.show()
