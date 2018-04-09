#!/usr/bin/env python3
#=====================================================================
#                       General Documentation 
"""Main program module. 
   Read Data from 'ASFG_Ts.txt' and visualize the 
   graph of surface temperatures with respect to the Julian days 
"""

#---------------------------------------------------------------------
#                       Additional Documentation 
# Notes: 
# - Written for Python 3.5.2
# - See import statements throughout for more informatino on 
#   non-built-in packages and modules required. 
#=====================================================================

#- Import Statements 

import numpy as np
import numpy.ma as ma 

#- reads text file and store each line as an element in the list by 
#  utilizing fileI/O object 
 
fileobj = open('ASFG_Ts.txt', 'r')
contents = fileobj.readlines()
fileobj.close()

#- build mask numpy array for Julian days and surface temperatures
#    in size of the number of data. Also, create a list for checking 
#    whether to mask the data. 
# (Note: subtracting 4 in the array because of the first 3 lines for
#     descriptions and the last line) 

jDay = ma.zeros(len(contents) - 4, 'd')
temps = ma.zeros(len(contents) - 4, 'd')
mask = []

#- iterating throughout the data sets by line and spliting into 
#   a list of strings. Then store the Julian day value and the
#   surface temperature into mask arrays and check the mask list 
#   if the surface temperature has valid data. 

for i in range(len(contents))[3:-1]:
    data = contents[i].split('\t')
    jDay[i - 3] = float(data[0]); 
    if len(data) < 4 or data[3] == '\n':
        mask.append(1)
    else:
        temps[i - 3] = float(data[3][:-1])
        mask.append(0)

#- mask the invalid data of the temperatures and Julian day 
#    with a list of mask.  

temps.mask = mask
jDay.mask = mask

#- print mean, median, and standard deviation of valid 
#    surface temperatures to the console. 

print(temps.mean())
print(np.ma.median(temps))
print(np.ma.std(temps))
    
#- Import Statements: for visualization 

import matplotlib.pyplot as plt 

#- Utilize scatter plot to build a graph of Surface temperature with 
#   respect to Julian days. 
 
plt.scatter(jDay, temps, s=1)
plt.title('Surface temperatures')
plt.xlabel('Julian Day (from 1/1/97)')
plt.ylabel('Surfacetemperature(deg C)')
plt.show()
# plt.savefig('name.png')