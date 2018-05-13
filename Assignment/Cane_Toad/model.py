import numpy as np
import numpy.ma as ma
from environment import Environment
import matplotlib.pyplot as plt 
import matplotlib.colors as colors

class Model(object): 
    
    def __init__(self):
        # CONSTANTS
        # for AWP init 
        self.AMT_AWP = 1
        self.AMT_AWP_ADJACENT = 0.4
        self.AMT_AWP_OVER2 = 0.2 
        
        self.WOULD_LIKE_EAT = 0.9 
        self.WOULD_LIKE_DRINK = 0.9
        
        
        # For Env 
        #initializing food and water value 
        self.PERCENT_AWPS = 0.01 
        self.PERCENT_AWPS_FENCED = 0.7
        self.FOOD_CELL = 0.03
        self.INIT_PERCENT_TOADS = 1.0
        self.MAY_HOP = 0.5 # Toad movement 
        
        
        # FOR RUNNING SIMULATION 
        self.CYCLES = 1200
        self.phase = 0
        self.numAlive = 0
        self.numCroaked = 0
        self.numMigrated = 0 
        
        self.figure = None
        self.axes = None
        self.image = None 
    
    def simulation(self): 
        self.execute_each_step()
        self.visualization()
        for i in np.arange(self.CYCLES): 
            self.execute_each_step()
            self.execute_each_step()
            self.execute_each_step()
            self.visualization()
            print("step: ", i)
            self.printStatus()
            
    def visualization(self): 
        self.axes = plt.gca()
        plt.ion()
        
        # data for foods 
        foodGrid = ma.masked_array(self.env.foods, self.env.foods < 0.0)
        cmap = colors.ListedColormap(['0.2', '0.3'])
        bounds = [0, self.FOOD_CELL, self.FOOD_CELL + 1]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        self.axes.imshow(foodGrid, cmap=cmap, norm=norm)        
        
        # data for awps 
        awpsGrid = ma.masked_array(self.env.awps, self.env.awps < 0.1)
        cmap = colors.ListedColormap(['0.05', '0.1', 'b'])
        bounds = [0.1, 0.3, 0.6, 1.1]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        self.axes.imshow(awpsGrid, cmap=cmap, norm=norm)
        
        # data for borders
        borderGrid = ma.masked_array(self.env.foods, self.env.foods > -0.5)
        cmap = colors.ListedColormap(['k'])
        bounds = [-2, 0]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        self.axes.imshow(borderGrid, cmap=cmap, norm=norm)        
        
        # data for toads 
        toadsGrid = ma.masked_array(self.env.toads_here, self.env.toads_here < 0.5)
        cmap = colors.ListedColormap(['c'])
        bounds = [0, 2]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        self.axes.imshow(toadsGrid, cmap=cmap, norm=norm)
        
        
        """
        self.axes.set_xlim(0, 42)
        self.axes.set_ylim(0, 42)
        self.axes.xaxis.set_major_locator(plt.MultipleLocator(1.0))
        self.axes.yaxis.set_major_locator(plt.MultipleLocator(1.0))
        self.axes.grid(which='major', axis='x', linewidth=0.75, linestyle='-', color='0.75')
        self.axes.grid(which='major', axis='y', linewidth=0.75, linestyle='-', color='0.75')"""
        self.axes.set_xticklabels([])
        self.axes.set_yticklabels([])
        plt.draw()
        plt.pause(0.001)
        plt.show()
    
    def printStatus(self):
        print("numAlive= ", self.numAlive)
        print("numMigrated= ", self.numMigrated)
        print("numCroaked= ", self.numCroaked)
    
    # Simulation Driver to be executed each time step 
    def execute_each_step(self):
        if self.phase == 0:
            self.phase_zero()
        elif self.phase == 1: 
            self.phase_one()
        elif self.phase == 2:
            self.phase_two()
        else:
            self.phase_three()
    
    # Phase 0: Initialization phase 
    def phase_zero(self):
        self.env = Environment(self)
        self.numAlive = len(self.env.toads)
        self.phase = 1  
    
    # consumption phase of the simulation driver
    def phase_one(self): 
        self.env.feed_toad()
        self.env.drink_toad()  
        self.phase = 2
        
    def phase_two(self): 
        self.env.move_toad()
        self.phase = 3
        
    def phase_three(self):
        dnumAlive, dnumCroaked, dnumMigrated = self.env.updateCount()
        self.numAlive += dnumAlive
        self.numCroaked += dnumCroaked 
        self.numMigrated += dnumMigrated 
        self.phase = 1 

        

model = Model()
list_alive = np.zeros(100, dtype=int)
list_migrated = np.zeros(100, dtype=int)
for i in np.arange(1): 
    model.simulation()
    list_alive[i] = model.numAlive
    list_migrated[i] = model.numMigrated
    

        
    