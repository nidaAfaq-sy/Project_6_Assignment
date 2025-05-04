# Python Dog Class Example

This project demonstrates how to create a simple `Dog` class in Python with attributes and methods. The class has a constructor to initialize the dog's name and breed, and a method to simulate a dog barking.

## 🧠 Concepts Used

- Class Definition
- Constructor (`__init__`)
- Methods
- Object Creation

## 📌 Code Overview

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says : woof woof")  


# Example usage
if __name__ == "__main__":
    dog1 = Dog("Buddy", "Aidi")
    dog1.bark()
