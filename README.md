# Python OOP Assignments – README

This project contains 21 Python Object-Oriented Programming (OOP) assignments that cover a wide range of OOP concepts such as classes, inheritance, decorators, access modifiers, abstract classes, and more.

---

## 1. Using `self`

**Objective:** Create a `Student` class with `name` and `marks` attributes initialized via the constructor using `self`, and a `display()` method to print student details.

## 2. Using `cls`

**Objective:** Create a `Counter` class to track how many objects have been created using a class variable and a class method with `cls`.

## 3. Public Variables and Methods

**Objective:** Create a `Car` class with a public variable `brand` and a public method `start()`. Instantiate the class and access both members from outside the class.

## 4. Class Variables and Class Methods

**Objective:** Create a `Bank` class with a class variable `bank_name`. Use a class method `change_bank_name(cls, name)` to modify it and show how it affects all instances.

## 5. Static Variables and Static Methods

**Objective:** Create a `MathUtils` class with a static method `add(a, b)` that returns the sum. No class or instance variables are used.

## 6. Constructors and Destructors

**Objective:** Create a `Logger` class that prints a message when an object is created (via constructor) and another when it is destroyed (via destructor).

## 7. Access Modifiers: Public, Protected, and Private

**Objective:** Create an `Employee` class with:

* Public variable: `name`
* Protected variable: `_salary`
* Private variable: `__ssn`
  Try accessing all from an object and observe behavior.

## 8. The `super()` Function

**Objective:** Create a base class `Person` with a constructor to set `name`. Inherit a `Teacher` class that uses `super()` to call the base constructor and adds `subject`.

## 9. Abstract Classes and Methods

**Objective:** Use the `abc` module to create an abstract class `Shape` with an abstract method `area()`. Inherit a class `Rectangle` that implements the method.

## 10. Instance Methods

**Objective:** Create a `Dog` class with instance variables `name` and `breed`. Add a method `bark()` that prints a message with the dog’s name.

## 11. Class Methods

**Objective:** Create a `Book` class with a class variable `total_books`. Add a class method `increment_book_count()` to update the book count.

## 12. Static Methods

**Objective:** Create a `TemperatureConverter` class with a static method `celsius_to_fahrenheit(c)` that returns the Fahrenheit value.

## 13. Composition

**Objective:** Create `Engine` and `Car` classes. Use composition by passing an `Engine` object to the `Car` class during initialization and calling an engine method from the car.

## 14. Aggregation

**Objective:** Create `Department` and `Employee` classes. Use aggregation by having `Department` store a reference to an existing `Employee` object.

## 15. Method Resolution Order (MRO) and Diamond Inheritance

**Objective:** Create four classes:

* `A` with `show()` method
* `B` and `C` inherit from `A` and override `show()`
* `D` inherits from both `B` and `C`
  Create an object of `D` and call `show()` to observe MRO.

## 16. Function Decorators

**Objective:** Write a decorator function `log_function_call` that prints "Function is being called" before a function runs. Apply it to `say_hello()`.

## 17. Class Decorators

**Objective:** Create a class decorator `add_greeting` that adds a `greet()` method to a class, returning "Hello from Decorator!". Apply to `Person` class.

## 18. Property Decorators: `@property`, `@setter`, `@deleter`

**Objective:** Create a `Product` class with private attribute `_price`. Use:

* `@property` to get price
* `@price.setter` to set price
* `@price.deleter` to delete price

## 19. `callable()` and `__call__()`

**Objective:** Create a `Multiplier` class that sets a `factor` using `__init__()` and multiplies input using `__call__()`. Test with `callable()`.

## 20. Creating a Custom Exception

**Objective:** Create a custom exception `InvalidAgeError`. Define a function `check_age(age)` that raises it if age < 18, and handle using `try...except`.

## 21. Make a Custom Class Iterable

**Objective:** Create a `Countdown` class that takes a starting number. Implement `__iter__()` and `__next__()` to iterate down to 0 using a for-loop.

---

### Prepared by Nida
