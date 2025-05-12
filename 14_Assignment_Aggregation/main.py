# Employee class
class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def display(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")


# Department class with aggregation
class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation (Employee passed as reference)

    def display(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()


# Creating an Employee object (independent of Department)
emp1 = Employee(101, "Nida")

# Creating a Department object and passing the Employee object
dept1 = Department("IT", emp1)

# Displaying Department details along with associated Employee
dept1.display()
