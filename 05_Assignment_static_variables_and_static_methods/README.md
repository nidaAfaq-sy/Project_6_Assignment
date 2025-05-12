# MathUtils

A simple Python class demonstrating the use of **static methods**.

## Description

`MathUtils` is a utility class containing a static method `add(a, b)` that returns the sum of two numbers.  
No class-level or instance-level variables are used. This is purely a demonstration of how to use `@staticmethod` in Python.

## Features

- Static method `add(a, b)` for addition
- No need to create an object to use the method

## Usage

```python
from math_utils import MathUtils  # If placed in a separate file named math_utils.py

result = MathUtils.add(10, 20)
print("Sum:", result)  # Output: Sum: 30
