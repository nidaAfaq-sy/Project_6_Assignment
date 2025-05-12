# 🧠 Method Resolution Order (MRO) and Diamond Inheritance in Python

This project demonstrates the concept of **Method Resolution Order (MRO)** in Python using a classic **diamond inheritance** pattern.

## 📚 Description

We define four classes:

- **A**: A base class with a method `show()`.
- **B** and **C**: Both inherit from **A** and override the `show()` method.
- **D**: Inherits from both **B** and **C** (diamond inheritance).

We then create an instance of class **D** and call the `show()` method to observe how Python resolves method calls through MRO.

## 🧾 Code Structure

```python
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

obj = D()
obj.show()

print("MRO:", D.__mro__)
