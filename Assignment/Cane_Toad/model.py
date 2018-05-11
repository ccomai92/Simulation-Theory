from .environment import Environment
from .toad import Toad 

class Model(object): 
    
    def __init__(self):
        # CONSTANTS
        
        # for AWP init 
        self.AMT_AWP = 1
        self.AMT_AWP_ADJACENT = 0.4
        self.AMT_AWP_OVER2 = 0.2
        
        # for initializing toad
        self.AMT_MIN_INIT = 0.88 
        
        self.DESSICATE = 0.6 
        self.STARVE = 0.6 
        self.ENERGY_FOR_HOPING = 0.002
        self.WATER_FOR_HOPING = 0.002  
        self.WOULD_LIKE_EAT = 0.9 
        self.WOULD_LIKE_DRINK = 0.9
        self.AMT_EAT = 0.01
        self.AMT_DRINK = 0.05 
        
        # For Env 
        #initializing food and water value 
        self.PERCENT_AWPS = 0.01 
        self.PERCENT_AWPS_FENCED = 0.2
        self.FOOD_CELL = 0.05 
        self.FRACTION_WATER = 0.6 
        self.INIT_PERCENT_TOADS = 0.8 
        self.INIT_RANGE = 0.12  
        self.MAY_HOP = 0.5 # Toad movement 
        
        
        # FOR RUNNING SIMULATION 
        self.dt = None 
        self.numAlive = 0
        self.numCroaked = 0
        self.numMigrated = 0 
        
        self.plot_figure = None
        self.plot_axes = None
        self.plot_image = None 

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
        self.env = Environment(self.PERCENT_AWPS, self.PERCENT_AWPS_FENCED)
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
        dnumAlive, dnumCroaked, dnumMigrated = env.toads.update()
        self.numAlive += dnumAlive
        self.numCroaked += dnumCroaked 
        self.numMigrated += dnumMigrated 
        self.phase = 1 

        """env = Environment(percent_awps, fraction_awps_fenced)
        self.env_list.append(env)
        init_toads_mask = np.random.binomial(1, env.init_percent_toads,\
                        size=(self.length - 2), type=bool)
        for i in range(1, np.size(init_toads_mask)):
            if (init_toads_mask[i]): 
                env.list_toads.append(Toad(x_init = env.width - 1, \
                                           y_init = 1, env=env))
                """
        
        
        
    