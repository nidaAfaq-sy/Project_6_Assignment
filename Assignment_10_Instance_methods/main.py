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
