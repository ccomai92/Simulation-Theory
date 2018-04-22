#==============================================================================
# Matplotlib example using objects and arbitrary placement
#
# By Johnny Lin
# May 2015
#
# Notes:
# * See:  http://nbviewer.ipython.org/github/ivanov/AY250/blob/
#   d26763380d05b046359b71f42298de3385338eb6/matplotlib_beyond_basics.ipynb
# * Advanced Guide:  http://matplotlib.org/users/developer.html
#==============================================================================


import matplotlib.pyplot as plt
import numpy as N


#- Arbitrary overlapping plots on a figure:

fig1 = plt.figure()

ax1 = fig1.add_axes((0.0, 0.2, 0.2, 0.8))  #+ input: left, bott, width, height
ax2 = fig1.add_axes((0.7, 0.7, 0.2, 0.2))
ax3 = fig1.add_axes((0.1, 0.1, 0.3, 0.3))
ax4 = fig1.add_axes((0.5, 0.5, 0.4, 0.1))

ax1.set_xticks([])
ax2.axis('off')
ax3.set_yticks([])
ax4.set_axis_bgcolor('y')

ax1.plot([1,2,3],[2,5,-3], 'bo-')
ax2.plot([5,9,10],[1,2,3], 'gx-.')
ax3.plot([4,6,8],[3,-5,2], 'rs--')


#- Arbitrary plots with various images and lines being drawn:

fig2 = plt.figure()
plt.ion()              #+ turn interactive on

ax1 = fig2.add_axes((0.0, 0.2, 0.2, 0.8))
ax2 = fig2.add_axes((0.7, 0.7, 0.2, 0.2))
ax3 = fig2.add_axes((0.1, 0.1, 0.3, 0.3))
ax4 = fig2.add_axes((0.5, 0.5, 0.4, 0.1))

for i in range(len(fig2.axes)):        #- Loop through all Axes in figure
    ax = fig2.axes[i]
    ax.axis('off')

    if i == 1 or i == 2:               #+ plot the sine curves, animated
        x = N.arange(20)*0.5
        y = N.sin(x)
        line, = ax.plot(x, y)
        for it in range(19):
            x = x + 0.5
            line.set_xdata(x)
            line.set_ydata(N.sin(x))
            plt.draw()
            plt.pause(0.1)

    else:                              #+ plot the images, animated
        x = N.arange(29) * 10.0
        y = N.arange(21) * 10.0 - 100.0
        data = N.outer( N.sin(y*N.pi/360.) \
                        , N.cos((x-140.)*N.pi/360.))
        img = ax.imshow(data, interpolation='none', cmap=plt.cm.rainbow,
                        extent=[0, 28, 0, 20],
                        aspect='auto',
                        zorder=0)
        for it in range(39):
            x = N.arange(29) * 10.0
            y = y + 20.0
            data = N.outer( N.sin(y*N.pi/360.) \
                            , N.cos((x-140.)*N.pi/360.))
            img.set_data(data)
            plt.draw()
            plt.pause(0.05)


#- Show all figures:

plt.show()