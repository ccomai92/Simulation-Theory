#env.py 
#model.py 
#toad.py 
#visualize.py 
#__init__.py -> from .model import Model 


#model.py 
# _string_test, dt(timestep, using default), numAlive, numCroaked, numMigrated
# plot figure, plot axes, plot image, fraction_awps_fenced
# list environ[], length = 42 width = 42, percent_AWPS = 0.01  
# 
#def environ_toad_init(): -initilize the environment and toads at the starting border
# create environment object 
# self.list environ.append(environ)
# np.randombinomial(1, environ.initpercenttods, size=(), astype(N.bool))
# for i in range(1, np.size(init_toads_mask_along border)): 
#   if init_toads_mask_along_boarder[i]:
#       environ.list_toad.append(Toad(x_init environ.width -1, y_init = i, env = environ))
#
# for itoad in environ.list_toad:
#   environ.is_toad_here[itoad.loc[0], itoad.loc[1]] = True 2D_array
#  
# self.numAlive = len(environ.list_toad)

# def run_session_plot_out(self, numhrs=None):
# for number of hours / self.dt
#     self.sim_hrs = it * self.dt / 3600 
#     for itoad in self.list_environ[0].list_toad: // for flexibility
#        a, b, c, = itoad.update() 
#        self.numAlive += a
#        self.numCroaked += b
#        self.numDied += c 





# class Toad (Object):
# def __init__(env=None...):
#   self.availbleFood = 
#       self.environ.food[self.loc_in_environ[0], self.loc_in_environ[1]]
#       self.environ.moisture[self.loc_in_environ[0], self.loc_in_environ[1]]
#       
# def eat(self): 
#   amtEat = N.min([self.amt_eat, self.avilablefood, 1.0 - self.energy])
#   self.water = N.min([self.water + self.FractionWATEr * amtEat, 1.0])
#   return amtEat

# def drink(self):
#   self.water = N.min([self.water + self.AMT_DRINK, 1.0])
#
# def update(self):
# dnumAlive = 0 (change)
# dnumCroaked = 0 (change)
# dnumMigrated = 0 (change)
# self.environ.feed_toad(self)
# self.environ.drink_toad(self)
# self.environ.move_toad(self)

# if (self.water < self.DESSICATE) or (self.energy < self.STARVE):
#   self.environ.list_toad.remove(self)
#   del self
#   dnumAlive -=1 
#   dnumCroaked += 1 
# elif self.loc_inenviron[1] == 0: 
#   self.environ.list_toad.remove(self)
#   del self
#   dnumAlive -=1 
#   dnumMigrated += 1 
# return dnumAlive, dnumCroaked, dnumMigrated 

# class Environ(object): 
# def __init__(self, fraction_awps): 
#   self.percentawps_fenced = fraction_awps_fenced
#   self.length = 42 y 
#   self.width = 42 x 
#   self._init_borders() // private methods
#   self._init_awps()   // private methods
#   self._init_food()   // private methods
#   self.list_toad = [] 

# def _init_borders(): 
#   self.is_start_border = n.zeros(9self.length, self.width), dtype = np.bool)
#   self.is_start_border[:,-1] = True 
#   self.isfinish 
#   self.isFinishborder[:,0] = True 

#   self.istoads_ok = np.ones((self.elngth, self.width), dtype = bool)


# def 
# self.is_awp = (np.randombinomial(1, self.Percent_AWPS, size=(self.length, self.width)) \
#               * self.is_toads_ok \
#               * np.logical_not(self.is_start_boarder) \
#               * np.logical_not(self.is_finish_border)).astype(N.boo)
#   multiply boolean !!!! 
# 
#  self.numawps = np.sum(self.is_awp)
#   self.num_fenced_awps = intself.num_awps *PERCENT_AWPS_FENCED)
#   self.num_unfenced_awps = self.num_awps - self.num_fenced_awps

# creating fences 
# 
# self.food = initialize all the foods to 1 
# def feed_toad(self, inToad):
#   amtEat  intToad.eat()
#   self.food[inToad.loc_in_environ[0], inToad.loc_in_environ[1]] -= amtEat

# def drink_toad(self, inToad): 
#   

# def moveToad(self): 
# 
# def hop_for_fun(self, inToad): 
#   loc = np.array([inToad.locx, inToad.locy])
#   if loc[1] == self.width - 1: 
#       if not self.is_toad_here[loc[0], loc[1]-1]: 
#           loc[1] -= 1
#   else: 
#       open_dirn = []
#       for i in [loc[0] - 1, loc[0], loc[0] + 1]:
#           for j in [loc[1] -1, loc[1]], loc[1] + 1]: 
#               if (i != loc[0] and j != loc[1]): 
#                   if not self.is_toad_here[i, j]:
#                       open_dirn.append((i, j))
#       np.random.shuffle(open_dirn)
#       try: 
#           loc=np.array(open_dirn[0])
#       except: no where to go so stay where you are 
#           loc = np.array([inToad.locX, inToad.locY])
#   return loc 

# def look_for_moisture(self, inToad):
#   loc = np.array([inToad.locX, inToad.locY])
#   neighbor_x = loc[1] + np.array([-1, 0, 1, 1, 1, 0, -1, -1])
#   neighbor_y = loc[0] + np.array([-1, -1, -1, 0, 1, 1, 1, 0])
        # np.where() returns tuple 
#   keep_pts, = np.where(\
#                np.logical_and(\
#                    np.logical_and(neighbor_x < self.width, neighbor_x >= 0),
#                    np.logical_and(neighbor_y < self.length, neighbor_y >= 0)))
#   neighbor_x = neighbor_x[keep_pts]
#   neighbor_y = neighbor_y[keep_pts]

# neighbor_moist = \
#   np.array([self.moisture[neighbor_y[i]], neighbor_x[i]]\ getting the moisture of the neighbor
#           for i in range(np.size(neighbor_x))])
#   max_values, = np.where(np.isclose(neighbor_moist, np.max(neighbor_moist)))
#   max_moist_x = np.array([neighbor_x[i] for i in max_values])
#   max_mosit_y = np.array([neighbor_y[i] for i in max_values])
#   max_moist = np.array([neighbor_moist[i] for i in max_values])
#   select = np.arange(np.size(max_moist))
#   np.random.shuffle(select)
#   return np.array([max_moist_y[select[0]], max_moist_x[select[0]]])

# np.isclose() compares two floating point values if they are similar
