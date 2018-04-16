"""
Data Error:
   cannot represent 
   Calibration error 
   
Modeling Error: 
   assumptions or system is incorrect 
   
Implementation Error: 
    Syntax, fat finger, units incorrect 
    
Truncation Error: 
    infinite series with finite terms 
    ex) Euler's method and exponential function 
    
Round off error: 
    limited number of bytes for your # 
 
Floating point: 
    storage method can introduce error (dataerror)
    comparison of floating points is inexact 
    
over and underflow 
    Too big or Too small can't be hold into data type 

Violation of numerical properties 
    error compounds as going through the loop 
    
    
Python 2.7: Sys.maxint tells max integers that can have 
Python 3.x don't have such 

Sys.float_info.min_10_exp / tells who small numbers can be

    Avoid division /save til last 

    integers are your friend 
    multiply instead of successive adds 

    avoid area around over and underflows 

    safe comparisons 

    be careful with very large and very small numbers

    avoiding type cast between different sized variables (large to small cast)

computational instability 
    
    Process: 
        What is changing? T
        How does it change? 
            changing relative to what? t
            
        Tnew = Told + dT/dt * deltaT
"""

k = -1.335
T0 = 100.0

num_ts = N.ceil(((end_time - start_time)/ delta_t) + 1)
times = (N.arange(num_pts) * delta_t) + start_time
temps = N.zeros(N.shape(times)) 

temps[0] = T0 

for i in range(1, N.size(times)): 
    temp[i] = temps[i-1] + (dTdt(k, temps[i-1]) * delta_t)
    
plt.plot(times, temps) 
plt.xlabel("Time[hrs]")
plt.ylabel("Temperatures [deg(c)]")

"""
Figure: Represents the whole figure window / page 
    command: figure, subplots 

Axes: represents a plot part inside the figure object(frame)
    command: subplots, add_axes (in arbitrary location) 
    
line2D: control the lines on a plot 

AxesImage: returned imshow function and is an image plot 
    change image data using set_data 
"""

fig1 = plt.figure() 

ax1 = fig1.add_axes((0.0, 0.2, 0.2, 0.8)) #input: left, bott, width, height 