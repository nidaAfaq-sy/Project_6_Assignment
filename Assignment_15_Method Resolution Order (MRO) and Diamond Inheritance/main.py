class A:
    def show(self):
        print("Show from class A")

class B(A):
    def show(self):
        print("Show from class B")

class C(A):
    def show(self):
        print("Show from class C")

class D(B, C):
    pass

# Create object of class D
obj = D()

# Call show() method
obj.show()

# Print the Method Resolution Order
print("MRO:", D.__mro__)
