# Define the Car class
class Car:
    # Public variable
    brand = "Toyota"
    
    # Public method
    def start(self):
        print("The car is starting...")

# Instantiate the class
my_car = Car()

# Access the public variable and method from outside the class
print(f"The car brand is: {my_car.brand}")
my_car.start()
