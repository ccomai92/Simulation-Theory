import numpy as np

class Toad(object): 
    
    def __init__(self, y, env=None):
        self.x = 41
        self.y = y
        
        self.env = env
        self.food_available = \
            self.env.foods[self.y, self.x]
        self.water_available = \
            self.env.awps[self.y, self.x]
        
        self.INIT_RANGE = 0.72
        self.energy = np.random.uniform(0.6, self.INIT_RANGE)
        self.water = np.random.uniform(0.6, self.INIT_RANGE)
    
        self.AMT_EAT = 0.01
        self.AMT_DRINK = 0.05
        self.DESSICATED = 0.6
        self.STARVE = 0.6
        self.FRACTION_WATER = 0.6 
        
        self.ENERGY_FOR_HOPING = 0.002
        self.WATER_FOR_HOPING = 0.002  
        
    def eat(self): 
        if (self.food_available > 0):
            amtEat = np.min([self.food_available, 1.0 - self.energy]) 
            self.water = np.min([(self.water + self.FRACTION_WATER * amtEat), 1.0])
            self.energy += amtEat
            self.env.foods[self.y, self.x] -= amtEat
            if self.env.foods[self.y, self.x] == 0:
                self.env.is_foods[self.y, self.x] = False
       
        
    def drink(self): 
        if (self.water_available > 0):
            original_water = self.water
            self.water = np.min([self.water + self.AMT_DRINK, 1.0])
            self.env.awps[self.y, self.x] -= (self.water - original_water)
            if self.env.awps[self.y, self.x] == 0: 
                self.env.is_awps[self.y, self.x] = False
        
    def hop_for_water(self): 
        if self.env.is_start_border[self.y, self.x]: 
            self.move_west() 
        elif self.env.awps[self.y, self.x] > 0: 
            self.stay_here() 
        elif self.env.awps[self.y, self.x] <= 0: 
            self.find_moisture()
    
    def hop_for_food(self): 
        if self.env.is_start_border[self.y, self.x]: 
            self.move_west() 
        elif self.env.foods[self.y, self.x] > 0: 
            self.stay_here() 
        elif self.env.is_foods[self.y, self.x] <= 0: 
            self.find_food()
    
    def find_food(self):    
        foods = np.array([-1, -1, -1, -1])
        
        if self.env.is_toads_ok[self.y + 1, self.x]: 
            north_food = self.env.foods[self.y + 1, self.x]
            foods[0] = north_food
        elif self.env.is_toads_ok[self.y - 1, self.x]: 
            south_food = self.env.foods[self.y - 1, self.x]
            foods[1] = south_food
        elif self.env.is_toads_ok[self.y, self.x + 1]: 
            east_food = self.env.foods[self.y, self.x + 1]
            foods[2] = east_food
        elif self.env.is_toads_ok[self.y, self.x - 1]: 
            west_food = self.env.foods[self.y, self.x - 1]
            foods[3] = west_food

    
        if (np.max(foods) == -1): 
            self.stay_here()
        else: 
            foods, = np.where(foods == np.max(foods))
            np.random.shuffle(foods)
            direction = foods[0]
            self.env.is_toads_ok[self.y, self.x] = True
            if direction == 0: 
                self.y += 1 
            elif direction == 1:
                self.y -= 1
            elif direction ==2:
                self.x += 1
            else:  
                self.x -= 1
            self.env.is_toads_ok[self.y, self.x] = False
            self.food_available = self.env.foods[self.y, self.x]
            self.water_available = self.env.awps[self.y, self.x]
            self.water_energy_for_hop()
            
    def hop_for_fun(self): 
        if self.env.is_start_border[self.y, self.x]: 
            self.move_west()
        else: 
            empty = np.array([False, False, False, False])
        
            if self.env.is_toads_ok[self.y + 1, self.x]: 
                empty[0] = True
            elif self.env.is_toads_ok[self.y - 1, self.x]: 
                empty[1] = True
            elif self.env.is_toads_ok[self.y, self.x + 1]: 
                empty[2] = True           
            elif self.env.is_toads_ok[self.y, self.x - 1]: 
                empty[3] = True 
                
            empty, = np.where(empty)
            np.random.shuffle(empty)
            if empty.size == 0: 
                self.stay_here()
            else: 
                direction = empty[0]
                self.env.is_toads_ok[self.y, self.x] = True
                if direction == 0: 
                    self.y += 1 
                elif direction == 1:
                    self.y -= 1
                elif direction ==2:
                    self.x += 1
                else:  
                    self.x -= 1
                self.env.is_toads_ok[self.y, self.x] = False
                self.food_available = self.env.foods[self.y, self.x]
                self.water_available = self.env.awps[self.y, self.x]
                self.water_energy_for_hop()
    
    def move_west(self): 
        if self.env.is_toads_ok[self.y, self.x - 1]:
            if self.env.is_toads_ok[self.y, self.x]: 
                self.env.is_toads_ok[self.y, self.x] = True
            self.x -= 1
            self.env.is_toads_ok[self.y, self.x] = False
            self.food_available = self.env.foods[self.y, self.x]
            self.water_available = self.env.awps[self.y, self.x]
            self.water_energy_for_hop() 
        else: 
            self.stay_here()
    
    def find_moisture(self):
        moistures = np.array([-1, -1, -1, -1])
        
        
        if self.y < 41 and self.env.is_toads_ok[self.y + 1, self.x]: 
            north_moisture = self.env.awps[self.y + 1, self.x]
            moistures[0] = north_moisture
        elif self.y > 1 and self.env.is_toads_ok[self.y - 1, self.x]: 
            south_moisture = self.env.awps[self.y - 1, self.x]
            moistures[1] = south_moisture
        elif self.x < 41 and self.env.is_toads_ok[self.y, self.x + 1]: 
            east_moisture = self.env.awps[self.y, self.x + 1]
            moistures[2] = east_moisture
        elif self.x > 1 and self.env.is_toads_ok[self.y, self.x - 1]: 
            west_moisture = self.env.awps[self.y, self.x - 1]
            moistures[3] = west_moisture

    
        if (np.max(moistures) == -1): 
            self.stay_here()
        else: 
            moistures, = np.where(moistures == np.max(moistures))
            np.random.shuffle(moistures)
            direction = moistures[0]
            self.env.is_toads_ok[self.y, self.x] = True
            if direction == 0: 
                self.y += 1 
            elif direction == 1:
                self.y -= 1
            elif direction ==2:
                self.x += 1
            else:  
                self.x -= 1
            self.env.is_toads_ok[self.y, self.x] = False
            self.food_available = self.env.foods[self.y, self.x]
            self.water_available = self.env.awps[self.y, self.x]
            self.water_energy_for_hop()
        
        
    
    def stay_here(self): 
         self.energy -= (self.ENERGY_FOR_HOPING * 0.5)
         if self.env.awps[self.y, self.x] == 0:
            self.water -= (self.WATER_FOR_HOPING * 0.5) 
    
    def update(self):
        dnumAlive = 0
        dnumCroaked = 0
        dnumMigrated = 0
        #self.env.feed_toad(self)
        #self.env.drink_toad(self)
        #self.environ.move_toad(self)
        
        if (self.water < self.DESSICATED) or (self.energy < self.STARVE):
            self.env.toads.remove(self)
            self.env.is_toads_ok[self.y, self.x] = True
            del self 
            dnumAlive -= 1
            dnumCroaked += 1
        elif (self.x == 0): 
            self.env.toads.remove(self)
            del self 
            dnumAlive -= 1
            dnumMigrated += 1 
        return dnumAlive, dnumCroaked, dnumMigrated
        
    def water_energy_for_hop(self): 
        self.energy -= self.ENERGY_FOR_HOPING
        self.water -= self.WATER_FOR_HOPING 
        
        