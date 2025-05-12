# Custom Exception class
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be at least 18.")
    else:
        return f"Age {age} is valid."

# Test the function with try...except
try:
    age = int(input("Enter your age: "))
    result = check_age(age)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid integer for age.")
