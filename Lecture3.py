# Documentation guide 
# Google docstring template
# reStructuredText 
#   formatting just using text characters 
#   * Item 1
#   * Item 2 
#   1. Item 1
#   2. Item 2 
"""def distance(x, y, pt): 
    import numpy as N 
    output_shape = (N.size(y), N.size(x))
    xall = N.resize(x, output_shape)
    yall = N.reshape(N.repeat(y, N.size(x)), output_shape)
    return (( (xall-pt[0]**2) + (yall - pt[1])**2))**0.5
# x and y coordinates at its locations """

"""
fobj = open('myfile.txt', 'r')
data = fobj.readlines() 
fobj.close() """

import numpy as np 
fobj = open('mytrig.txt', 'w')
angle = np.arange(101, dtype='d') / 100.0 * np.pi
sine = np.sin(angle)
cosine = np.cos(angle)
output = []
for i in range(np.size(angle)):
    output.append(str(angle[i]) + '\t' + str(sine[i]) + '\t' \
    + str(cosine[i]) + '\n')
    
fobj.writelines(output)
fobj.close() 

#--- 

fobj = open('mytrig.txt', 'r')
data = fobj.readlines() 
angle = np.zeros(len(data), dtype='d')
sine = np.zeros(len(data), dtype='d')
cosine = np.zeros(len(data), dtype='d')
for i in range(len(data)):
    temp = data[i]
    values = temp.split('\t')
    angle[i] = float(values[0])
    sine[i] = float(values[1])
    cosine[i] = float(values[2])
fobj.close()

# import matplotlib.pyplot as plt 
# plt.plot(angle, sine) 
# plt.title("My Sine')
# plt.plot(angle, cosine)
# plt.figure(2)
# plt.plot(angle, cosine) 
# 