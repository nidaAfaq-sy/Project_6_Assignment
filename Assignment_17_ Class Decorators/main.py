# Define the class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Testing the decorated class
p = Person("Nida")
print(p.greet())  # Output: Hello from Decorator!
