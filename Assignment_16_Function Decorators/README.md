# Function Decorator: `log_function_call`

This project demonstrates the use of a **function decorator** in Python. The decorator, named `log_function_call`, prints a message before executing the decorated function.

## Description

The `log_function_call` decorator prints `"Function is being called"` each time a decorated function is invoked. It’s a basic example to understand how decorators can be used for logging or other cross-cutting concerns.

## Files

- `main.py` – Contains the decorator definition and a sample function `say_hello()` using the decorator.

## Code Example

```python
# main.py

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello():
    print("Hello!")

say_hello()
