import numpy as np
from toad import Toad

class Environment(object): 
    
    def __init__(self, model):
        self.model = model
        self.length = 42 
        self.width = 42 
        self._init_borders()
        self._init_awps()
        self._init_foods() 
        self.toads = []
        self._init_toads()    

        
        
            
    def _init_borders(self):
        self.is_start_border = \
            np.zeros((self.length, self.width), dtype=bool)
        self.is_start_border[:, -1] = True 
        
        self.is_finish_border = \
            np.zeros((self.length, self.width), dtype=bool)
        self.is_finish_border[:,0] = True 
        
        self.is_north_border = \
            np.zeros((self.length, self.width), dtype=bool)
        self.is_north_border[0,:] = True 
        
        self.is_south_border = \
            np.zeros((self.length, self.width), dtype=bool)
        self.is_south_border[-1,:] = True     
        
        self.is_toads_ok = np.ones((self.length, self.width), dtype=bool)
        self.is_toads_ok = np.logical_and(self.is_toads_ok, \
                                np.logical_not(self.is_start_border)) 
        self.is_toads_ok = np.logical_and(self.is_toads_ok, \
                                np.logical_not(self.is_finish_border))
        self.is_toads_ok = np.logical_and(self.is_toads_ok, \
                                np.logical_not(self.is_north_border))
        self.is_toads_ok = np.logical_and(self.is_toads_ok, \
                                np.logical_not(self.is_south_border)) 
    
    def _init_toads(self):  
        for i in np.arange(1, self.is_start_border[:, -1].size - 1):
            create = np.random.binomial(1, self.model.INIT_PERCENT_TOADS)
            if create: 
                toad = Toad(i, self)
                self.toads.append(toad)
                
        self.toads_here = np.zeros((self.length, self.width), dtype=int)
        for toad in self.toads: 
            self.toads_here[toad.y, toad.x] = 1
         
              
    
    def _init_foods(self):
        self.is_foods = np.ones((self.length, self.width), dtype=bool)
        self.is_foods = np.logical_and(self.is_foods, \
                    np.logical_not(self.is_start_border))
        self.is_foods = np.logical_and(self.is_foods, \
                    np.logical_not(self.is_finish_border))
        self.is_foods = np.logical_and(self.is_foods, \
                    np.logical_not(self.is_north_border))
        self.is_foods = np.logical_and(self.is_foods, \
                    np.logical_not(self.is_south_border))
        self.foods = np.where(self.is_foods, self.model.FOOD_CELL, -1.0)
                    
    def _init_awps(self):
        #creating AWPS excluding start, finish boarder
        self.is_awps = \
            np.random.binomial(1, self.model.PERCENT_AWPS, size=(self.length, self.width))
                        
        self.is_awps = np.logical_and(self.is_awps, self.is_toads_ok)
        self.awps = np.where(self.is_awps, self.model.AMT_AWP, 0.0)
        y, x = np.where(self.is_awps)
        for i in np.arange(y.size):
            self._init_Awp(y, x)
            self._init_Awp2(y, x)
                                
        num_awps = np.sum(self.is_awps)
        self.num_fenced_awps = \
                int(num_awps * self.model.PERCENT_AWPS_FENCED)
        self._init_fenced_awps(y, x)
        y, x = np.where(np.logical_not(self.is_toads_ok))
        self.awps[y, x] = - 1
        
    def _init_fenced_awps(self, y, x):
        fence_it = np.random.binomial(1, \
                                    self.model.PERCENT_AWPS_FENCED,\
                                    size=self.num_fenced_awps)
        for i in np.arange(fence_it.size):
            if fence_it[i]:
                self.awps[y[i], x[i]] = -1 
                 
        
    def _init_Awp(self, y, x):      
        
        for i in np.arange(3) - 1: 
            for j in np.arange(3) - 1:
                current = self.awps[y + i, x + j]
                self.awps[y + i, x + j] = \
                        np.maximum(self.model.AMT_AWP_ADJACENT, current)
        
    def _init_Awp2(self, y, x):
        for i in np.arange(5) - 2:
            for j in np.arange(5) - 2:
                current = self.awps[y + i, x + j]
                self.awps[y + i, x + j] = \
                    np.maximum(self.model.AMT_AWP_OVER2, current)
        
        
        
    def feed_toad(self): 
        for toad in self.toads: 
            if (toad.energy < self.model.WOULD_LIKE_EAT) and \
            (toad.food_available > 0.0):
                toad.eat()
            
    def drink_toad(self): 
        for toad in self.toads:
            if (toad.water < self.model.WOULD_LIKE_DRINK) and \
            (toad.water_available > 0.0):
                toad.drink()  
            
    def move_toad(self):
        for toad in self.toads: 
            if toad.water <= self.model.WOULD_LIKE_DRINK: 
                self.toads_here[toad.y, toad.x] = 0
                toad.hop_for_water()
                self.toads_here[toad.y, toad.x] = 1
            elif toad.energy <= self.model.WOULD_LIKE_EAT:
                self.toads_here[toad.y, toad.x] = 0
                toad.hop_for_food() 
                self.toads_here[toad.y, toad.x] = 1
            elif np.random.uniform(0, 1) < self.model.MAY_HOP: 
                self.toads_here[toad.y, toad.x] = 0
                toad.hop_for_fun()
                self.toads_here[toad.y, toad.x] = 1
            else: 
                toad.stay_here()
            
    def updateCount(self): 
        resultAlive = 0
        resultCroaked = 0
        resultMigrated = 0
        for toad in self.toads:
            dnumAlive, dnumCroaked, dnumMigrated = toad.update()
            if dnumCroaked > 0:
                self.toads_here[toad.y, toad.x] = 0
            resultAlive += dnumAlive
            resultCroaked += dnumCroaked
            resultMigrated += dnumMigrated
        return resultAlive, resultCroaked, resultMigrated
        