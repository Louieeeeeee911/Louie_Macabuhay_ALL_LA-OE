class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    
    def describeVehicle(self):
        print(f"{self.model} is a {self.brand} and has {self.fuel_type}")
        
class car(Vehicle):
    pass     
        
carBrand = Vehicle("Toyota", "Hilux", "Diesel")
carBrand.describeVehicle()

class Motorcycle(Vehicle):
    pass

motor = Motorcycle("Yamaha", "Mio", "Unleaded gas")
motor.describeVehicle()
