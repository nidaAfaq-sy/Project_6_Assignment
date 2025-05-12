class Counter:
    # Class variable to store the count
    count = 0
    
    def __init__(self):
        # Increment the count every time an object is created
        Counter.count += 1
    
    @classmethod
    def display_count(cls):
        # Class method to display the count of objects created
        print(f"Total objects created: {cls.count}")

# Test the Counter class
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()

# Display the total count of objects created
Counter.display_count()  # Output: Total objects created: 3
