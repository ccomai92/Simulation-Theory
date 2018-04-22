# -*- coding: utf-8 -*-
# SD models: ODE (System dynamics models)
# Monte Carlo method: 
#   models: Non-deterministic 
#   Simulations vs. Ensembles of Simulations 
#   
# Cellular Automata models: Intro, Grids, Boundaries 
#   = finite elements 
#   = finite difference 
# 
# Diffusion: 
#   - What's being simulated
#       simulating the movement of heat in the calculation of temperature
#   - provide definition of Diffusion 
#       high T -> transfers heat -> low T 
#********* Conduction (전도) Mechanism ****************** 

# Convection: (기체나 액체에 의한 열의) 대류
# Radiation: electro magnetic waves 

# 1. Big -> chop it up into pieces -> 
# 2. ****Pieces are fixed -> contradicted to -> agent-based models 

# Assumptions in models: 
#   consistent cell structure 
#   rule is consistent for each cell 
#   assuming that discrete measurements of T is ok 
#   size of each cell is consistent throughout the simulation though 
#       it can be changed
#       -> properties of the bar associated with simulation. 
#       -> r would change in a melted bar. 
#   Cells from same material 
#       r would change between cells depending on material 
#           (store array of r values)
#   Diff model: moore vs. von-neuman 
#   Single cell is uniform or a single entity ()
#       also assuming that discrete measurements of T is ok 
#   Environment T no change 
#   Time interval is finite and constant 
#   2D not 3D, 2D is enough (assumption)

# ********* How to test the assumptions ********* 
#   - After alter the simulation and then re-run 
#       * Sensitivity test is common 
#       * just give some sense of relative behavior 


#******************* Grids ****************************
# Rectangular Grid 
# Finite element grid  
#   mesh is not regular 
# Adaptive grid:
#    1. higher desity of points when there is need 
#    2. Aero dynamics or fluid dynamics model 
# Geodesic grid 
#    polygonal boxes 
#    pole problem 
# Staggered Grid 
#    choice of staggering 
#    choice matters with respects to the simulaiton
# Spectral method  
#   FFT: frequency domain to time domain 
#   Start out with the that is regular 
#   2D waves (fourier) and back to regular 

#******************** Boundaries ***********************
# 3 Kinds of boundary conditions 
#   Reflective BC = same as adjacent (ventilated )
#   Absorbing b.c. : Default value (from the env = ambient)(bar)
#   Period b.c. : wrap around (Cylinder)
#   Ghost cells (points)