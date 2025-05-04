📘 Python OOP Assignments – README
👩‍💻 About
This repository contains 21 Python Object-Oriented Programming (OOP) assignments designed to help you understand core OOP concepts using practical examples. Each assignment demonstrates specific principles like inheritance, polymorphism, decorators, access modifiers, and more.

🧾 Assignment List
1. Using self
Create a Student class.

Initialize name and marks using self in the constructor.

Add a display() method to print student details.

2. Using cls
Create a Counter class to count how many objects are created.

Use a class variable and class method (cls) to track and display count.

3. Public Variables and Methods
Create a Car class with a public variable brand and a public method start().

Access both from outside the class.

4. Class Variables and Class Methods
Create a Bank class with class variable bank_name.

Use a class method change_bank_name() to modify it across all instances.

5. Static Variables and Static Methods
Create a MathUtils class with a static method add(a, b) to return their sum.

No use of class or instance variables.

6. Constructors and Destructors
Create a Logger class that prints a message when created and another when destroyed.

7. Access Modifiers
Create an Employee class with:

Public variable name

Protected variable _salary

Private variable __ssn

Demonstrate accessibility from an object.

8. The super() Function
Create a Person class and a Teacher subclass.

Use super() to inherit and extend constructor functionality.

9. Abstract Classes and Methods
Use abc module to define an abstract class Shape with method area().

Implement Rectangle that inherits and defines the area() method.

10. Instance Methods
Create a Dog class with instance variables and a method bark().

11. Class Methods
Create a Book class with class variable total_books.

Use increment_book_count() class method to update it.

12. Static Methods
Create a TemperatureConverter with a static method celsius_to_fahrenheit(c).

13. Composition
Create Engine and Car classes.

Use composition: Car class accepts an Engine object and uses its method.

14. Aggregation
Create Employee and Department classes.

Use aggregation: Department holds a reference to an Employee object.

15. Method Resolution Order (MRO)
Implement diamond inheritance with classes A, B, C, D.

Call method from class D to observe MRO.

16. Function Decorators
Write a decorator log_function_call that logs before executing any function.

Apply it to say_hello().

17. Class Decorators
Create a class decorator add_greeting that adds a greet() method to a class.

18. Property Decorators
Create a Product class with a private attribute _price.

Use @property, @setter, and @deleter for controlled access.

19. callable() and __call__()
Create a Multiplier class with __call__() to use object like a function.

Demonstrate using callable().

20. Custom Exception
Create a custom exception InvalidAgeError.

Function check_age() raises this exception if age < 18.

21. Iterable Class
Create a Countdown class that can be used in a for loop using __iter__() and __next__().

