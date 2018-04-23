#=============================================================================
# Random walk program
#
# Solution to Shiflet & Shiflet (2014)'s Module 9.5 program.
#
# By Johnny Lin
# April 18, 2015
#
# Notes:
# - About animation in matplotlib:
#   http://wiki.scipy.org/Cookbook/Matplotlib/Animations
#   http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
#   http://stackoverflow.com/questions/12822762/pylab-ion-in-python-2-
#       matplotlib-1-1-1-and-updating-of-the-plot-while-the-pro
#=============================================================================


#========================== USER ADJUSTABLE (begin) ==========================
N_TESTS = 100 #- number random walk tests
N_STEPS = 50  #- max. number of random walk steps to see how mean distance
              #  behaves
#=========================== USER ADJUSTABLE (end) ===========================


import numpy as N
import matplotlib.pyplot as plt


def randomWalkPoints(n):
    output_list_x = N.zeros((n,), dtype='l')
    output_list_y = N.zeros((n,), dtype='l')

    rand = N.random.randint(2, size=(n-1,))
    output_list_x[1:] = N.where(rand == 0, 1, -1)[:]
    output_list_x = N.cumsum(output_list_x)

    rand = N.random.randint(2, size=(n-1,))
    output_list_y[1:] = N.where(rand == 0, 1, -1)[:]
    output_list_y = N.cumsum(output_list_y)

    return (output_list_x, output_list_y)


def animateWalk(x_points, y_points):
    plt.ion()    #- Turn interative mode on

    mylines = plt.plot(x_points, y_points, "o-")  #- mylines is a list of
                                                  #  lines drawn by plot
    line = mylines[0]  #- there's only one line drawn by the above plot call
    plt.axis([-10, 10, 
              -10, 10])

    for i in range(N.size(x_points)):
        line.set_xdata(x_points[:i+1])
        line.set_ydata(y_points[:i+1])
        plt.draw()
        plt.pause(1)


def randomWalkDistance(x_points, y_points):
    return N.sqrt(x_points[-1]**2 + y_points[-1]**2)


def meanRandomWalkDistance(n, numTests):
    sumDist = 0.0
    for i in range(numTests):
        xpts, ypts = randomWalkPoints(n)
        sumDist = sumDist + randomWalkDistance(xpts, ypts)
    return float(sumDist) / numTests


xpts, ypts = randomWalkPoints(5)   #- Test the randomWalkPoints method
animateWalk(xpts, ypts)            #  using animation

mean_dist = N.zeros((N_STEPS,), dtype='d')
for i in range(1,N_STEPS):
    mean_dist[i] = meanRandomWalkDistance(i, N_TESTS)
    print("Mean distance: " + str(mean_dist[i]))

plt.figure(2)
plt.plot(N.arange(N_STEPS), mean_dist, 'o')
plt.show()
