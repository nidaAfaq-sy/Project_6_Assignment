class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name           # public variable
        self._salary = salary      # protected variable
        self.__ssn = ssn           # private variable

# Create object of Employee
emp = Employee("Nida", 70000, "123-45-6789")

# Accessing public variable
print("Public - Name:", emp.name)

# Accessing protected variable
print("Protected - Salary:", emp._salary)

# Accessing private variable directly (will raise error)
try:
    print("Private - SSN:", emp.__ssn)
except AttributeError as e:
    print("Private - SSN: Cannot access directly:", e)

# Accessing private variable using name mangling
print("Private - SSN (using name mangling):", emp._Employee__ssn)
