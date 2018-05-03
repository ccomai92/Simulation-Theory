# What Do Models Mean: Statistical and Graphical Measures 
# Purpose: How do you compare a model to something else in 
#         order to understand what the model is telling? 
# Key idea: You compare a model to something you understand
# Three Categories of methods we'll discuss: 
#   - Basic statistical analysis 
#   - Basic graphical analysis 
#   - More advanced statistical and graphical analysis 

# Comparing models to what? 
#   Data: 
#       MEasurements by people or instruments 
#       that you want your simulation to match
#   Intuition: 
#       Do certain special cases conform to what you can reasonably expect? 
#       A climate model, for instance, should produce a surface temperature 
#       distribution where it is warmer in the tropics than at the poles. 
#   Naive benchmark: 
#       Your model behaves/gives results that are "better" than 
#       some simple calculation. 
#           - Predictions that beat persistent: Do better than just 
#               saying "tomorrow will be the same as today" 
#           - Simulates major cycles: E.g., climatological (seasonal)
#               cycle in space and time. 
#           - Simulates a distribution of modes: Compare with the distribution
#               of a simple statistical model, e.g., first-order autoregressive
#               or first-order Markov model. 

# Basic Statistical analysis 
#   Purpose: Basic properties of the data, as a collection. 
#   "Central tendency": Mean (median is better). 
#   "Spread": Variance. 
#   "Connection between two variables": Correlation 
#   Mean and Variance(Mean of the (deviation from the mean)).
#    Correlation coefficient: Looks like the variance between x and y, divided
#    by the standard deviation of x and the standard deviation of y. 
#        - MEasures the degree to which two variables (e.g., x and y)
#            are linearly related 
#        - Values between -1 and 1 
#        - 0 means no correlation 
#        - 1 means increases in x are associated with increases in y (vice versa)
#        - -1 means increases in x are associated with decreases in y (vice versa) 

# Class Problem to do 
#   Write a correlation function using the definition of correlation, without 
#   using a pre-written 

import numpy as np 

def correlation(arrayX, arrayY):
    meanX = np.mean(arrayX)
    meanY = np.mean(arrayY)
    n = arrayX.size
    stdX = np.std(arrayX)
    stdY = np.std(arrayY)
    newX = arrayX - meanX
    newY = arrayY - meanY 
    newList = newX * newY
    sumList = np.sum(newList)
    sumList /= ((n-1)*stdX*stdY)
    return sumList 
"""
def correlation(x, y): 
    num = np.sum((x - average(x)) * (y - average(y)))
    den = (N.size(x) - 1.0) * N.sqrt(variance(x)) \
                * np.sqrt(variance(y)) 
    return num / den
""" 

# Is statistical anlysis enough? Motivation for graphical analysis 
#   not enough, std and mean is not enough 

# run sequence example 
#   Detect trends 
#   Detect whether there have been any shifts in the data 
#   Detext shifts in variability (variance) 

     
# Histogram Example 
#     Easiest way to count the number of occurrences within a bin 
#    Counts often normalized into a percentage of the total number of points 
#    Graphically shows 

# Normal Distribution 
#     - Central limit theorem: The some of many independent random variable
#        will converge to a normal distribution 
#    - Many phenomena are normally distributed, measurement erros, financial variables
#        yes or no questions 

# Lag plots 
#   Plot Xi vs Xi-1 
#   Checks whether the data is random 
#   Checks if there is serial correlation in the data
#   Also shows if there are any outliers in the data 
#   Black = y [:-1]
#   Purple = y[1:]
#   ex: strong serial corrleation 
#       no correlation (dust kind)

# Lag plots of sinusoidal data 
#   Circular data + outliers 

# More advanced statistical Graphical analysis 
# Lag-correlation analysis 
#   - correlation anlysis works when you have two timeseries you 
#    want to compare with each other 
#   - with lag correlation anlysis, you shift the two timeseries 
#    relative to each other and calculate the corrleation 

# predictibility 
#    not just x and y is related 
#   maybe early y may affect later x (something more than x and y relation)
#   in instantaneous time 

#   x(t), y(t - 1) r = 0.7
#   x(t), y(t - 10) r = 0.9 
#   lag required to disseminate (still linear correlation)
#   Help us to see causality 
#   

# Spectral Analysis 
#   Works on a single timeseries 
#   Based on Fourier analysis: can turn any function into an infinite sum of sine waves
#   Spectral power measures the magnitude of the component that has a certain 
#   frequency (period). 
#   - What is driving the series ?? 
#   

# Conclusions
#   "To compare model results, 
#   Stats and models are really useful" 

x = np.arange(100) * 0.01 * 4 * np.pi
y1 = np.sin(x)
y2 = np.sin(x) * 2

lags = np.arange(81) - 40
corr_coeffs = np.zeros(np.size(lags), dtype='d')
for i in range(np.size(lags)): 
    if lags[i] < 0:
        corr_coeffs[i] =  
    elif lags[i] > 0: 
    else: 