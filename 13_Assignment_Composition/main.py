# Engine class
class Engine:
    def start(self):
        return "Engine started."

# Car class using composition
class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition: Car "has-a" Engine

    def start_car(self):
        return self.engine.start()  # Accessing method of Engine via Car

# Creating an Engine object
my_engine = Engine()

# Passing the Engine object to the Car class
my_car = Car(my_engine)

# Accessing the start method of Engine through Car
print(my_car.start_car())  # Output: Engine started.
