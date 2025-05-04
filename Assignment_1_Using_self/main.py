class Student:
    def __init__(self, name, marks):
        # Using self to refer to instance attributes
        self.name = name
        self.marks = marks

    def display(self):
        # Display student details
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")

# Example usage
student1 = Student("Nida", 92)
student1.display()
