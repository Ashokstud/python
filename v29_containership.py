# Containership
'''
one class contains an instance of another class as one of its attributes 
'''
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine(200)  # Creating an instance of the Engine class as an attribute

    def display_info(self):
        print(f"{self.make} {self.model} with {self.engine.horsepower} horsepower")

# Creating an instance of the Car class
my_car = Car("Toyota", "Camry")

# Accessing and displaying information
my_car.display_info()
