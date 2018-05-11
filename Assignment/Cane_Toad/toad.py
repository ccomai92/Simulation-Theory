import numpy as np

class Toad(object): 
    
    def __init__(self, env=None):
        self.env = env
        self.avilableFood = \
            self.env.food[self.loc_in_environ[0], self.loc_in_environ[1]]
        self.avilableWater = \
            self.env.moisture[self.loc_in_environ[0], self.loc_in_environ[1]]
        
        self.AMT_EAT = 0.01
        self.AMT_DRINK = 0.05
        self.DESSICATED = 0.6
        self.STARVE = 0.6
        self.FRACTION_WATER = 0.6 
        
    def eat(self): 
        amtEat = np.min([self.amt_eat, self.availablefood, 1.0 - self.energy]) 
        self.water = np.min([(self.water + FRACTION_WATER * amtEat), 1.0])
        return amtEat
        
    def drink(self): 
        self.water = np.min([self.water + self.AMT_DRINK, 1.0])
    
    def update(self):
        dnumAlive = 0
        dnumCroaked = 0
        dnumMigrated = 0
        #self.env.feed_toad(self)
        #self.env.drink_toad(self)
        #self.environ.move_toad(self)
        
        if (self.water < self.DESSICATE) or (self.energy < self.STARVE):
            self.env.list_toad.remove(self)
            del self 
            dnumAlive -= 1
            dnumCroaked += 1
        elif (self.loc_inenviron[1] == 1): 
            self.env.list_toad.remove(self)
            del self 
            dnumAlive -= 1
            dnumMigrated += 1 
        return dnumAlive, dnumCroaked, dnumMigrated
        

        
        
        