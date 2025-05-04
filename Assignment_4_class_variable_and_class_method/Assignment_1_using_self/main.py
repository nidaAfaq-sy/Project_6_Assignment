class Student:
    def __init__(self, name, marks):
        self.name = name  # using self to initialize the name
        self.marks = marks  # using self to initialize the marks

    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Nida", 92)
student1.display()
