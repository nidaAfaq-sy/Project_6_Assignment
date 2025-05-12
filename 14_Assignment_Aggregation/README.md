# Aggregation Example: Department and Employee Classes

This project demonstrates the concept of **Aggregation** in Object-Oriented Programming using Python.

## 📚 Concept

**Aggregation** is a form of association where one class contains a reference to another class, but both can exist independently.

In this example:
- The `Department` class contains a reference to an `Employee` object.
- The `Employee` object exists independently of the `Department`.

## 📁 Files

- `main.py` - Contains the implementation of `Employee` and `Department` classes and the demonstration.

## 🧱 Classes

### Employee

Represents an individual employee.

**Attributes**:
- `emp_id` (int): Unique ID of the employee.
- `name` (str): Name of the employee.

**Methods**:
- `display()`: Prints employee details.

### Department

Represents a department in an organization.

**Attributes**:
- `dept_name` (str): Name of the department.
- `employee` (Employee): An employee assigned to the department.

**Methods**:
- `display()`: Prints department and associated employee details.

## ▶️ How to Run

Make sure you have Python installed. Then run:

```bash
python main.py
