class Car(object): # inherent from object, if nothing, just object class
    number_wheels = 4 #class variable (no self in front of it)
    
    def __init__(self, make, model, year): #constructor always named this way
        self.make = make 
        self.model = model
        self.year = year
        
    def write_summary(self): 
        print(self.make + " " + self.model \
            + " (" + str(self.year) + ")" \
            + " has " + str(Car.number_wheels) + " wheels") # or self.number_wheels
            
first_car = Car("Chevrolet", "Monza", 1980)
first_car.write_summary() 
print(first_car.number_wheels)
print(Car.number_wheels) 
    
    
# hasattr(first_car, 'make')
# a = getattr(first_car, 'make')
# setattr(first_car, 'make', 'Ford') 
# print(first_car.make)
# 