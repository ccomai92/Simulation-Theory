import numpy as np

class Environment(object): 
    
    def __init__(self, percent_awps, fraction_awps_fenced):
        self.percent_awps = percent_awps 
        self.percent_awps_fenced = fraction_awps_fenced
        self.length = 42 
        self.width = 42 
        self._init_borders()
        self._init_awps()
        self._init_food() 
        self.toads = []
        self._init_toads()     
            
    def _init_borders(self):
        self.is_start_border = \
            np.zeros((self.length, self.width), dtype=bool)
        self.is_start_border[:, -1] = True 
        self.is_finish_border = \
            np.zeros((self.length, self.width), dtype=bool)
        self.is_finish_border[:,0] = True 
        
        self.is_toads_ok = np.ones((self.length, self.width), dtype=bool)
    
    def _init_toads(self):  
    
    def _init_foods(self):
                    
    def _init_awps(self):
        #creating AWPS excluding start, finish boarder
        self.is_awps = \
                (np.random.binomial(1, self.percent_awps_fenced, \
                    size=(self.length, self.width)) \
                    * self.is_toads_ok \
                    * np.logical_not(self.is_start_border)\
                    * np.logical_not(self.is_finish_border)).astype=(np.bool)
                    
        self.num_awps = np.sum(self.is_awps)
        self.num_fenced_awps = \
                int(self.num_awps * self.percent_awps_fenced)
        self.num_unfenced_awps = self.num_awps - self.num_fenced_awps
        
        # creating fences 
        
    def placeFencedAwps(self):
        
        
    def initAwp(self): 
        
    def initAwp2(self):
        
    def feed_toad(self): 
        if (toads.energy < WOULD_LIKE_EAT):
            toads.eat()
        else:
            toads.amt_eat = 0
            
    def drink_toad(self): 
        if (toads.water < WOULD_LIKE_DRINK) and \
            (toads.water_available):
            toads.drink() 
            
    def move_toad(self):
        if toads.water < WOULD_LIKE_DRINK: 
            hop_for_water()
        elif toads.energy < WOULD_LIKE_EAT:
            hop_for_food() 
        elif np.random() < MAY_HOP: 
            hop_for_fun()
        else: 
            stay_here()
    
    def hop_for_water(self): 
        if (AWP[toads.y, toads.x]): 
            stay_here()
        elif (not AWP[toads.y, toads.x]): 
            # find moisture 
        elif (startBorder[toads.y, toads.x] and #west is empty):
            # move West 
        elif (startBorder )
            stay_here() 
            
    def move_west(self): 
        toads.x -= 1
        toads.availableFood = self.food[toads.y, toads.x]
        toads.availableWater = self.water[toads.y, toads.x]
        # reduce toad's water energy for hoping 
        