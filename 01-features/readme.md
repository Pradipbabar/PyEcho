# Advanced Python Features

## List Comprehensions, Lambda Functions, and Generators

### List Comprehensions
List comprehensions provide a concise way to create lists in Python. They allow you to generate a new list by applying an expression to each item in an existing iterable (e.g., a list or range).

```python
# Example: Squaring numbers using list comprehension
squared_numbers = [x**2 for x in range(1, 6)]
# Result: [1, 4, 9, 16, 25]
```

### Lambda Functions
Lambda functions (also known as anonymous functions) are short, one-line functions defined using the `lambda` keyword. They are useful for writing small, inline functions.

```python
# Example: Lambda function to calculate the square of a number
square = lambda x: x**2
print(square(5))
# Result: 25
```

### Generators
Generators provide an efficient way to iterate over large datasets by producing values one at a time, rather than creating an entire list at once. They are defined using functions with the `yield` keyword.

```python
# Example: Generator function to generate Fibonacci sequence
def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibonacci_sequence = list(fibonacci_generator(5))
# Result: [0, 1, 1, 2, 3]
```

## Decorators and Context Managers

### Decorators
Decorators are a powerful way to modify or extend the behavior of functions. They are applied using the `@decorator` syntax and are commonly used for tasks like logging, timing, or access control.

```python
# Example: Simple timing decorator
import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper

@timing_decorator
def example_function():
    # Some time-consuming operation
    time.sleep(2)
    print("Function executed.")

example_function()
```

### Context Managers
Context managers are used with the `with` statement to set up and tear down resources, such as opening and closing files. They are defined by implementing `__enter__` and `__exit__` methods in a class or using the `contextlib` module.

```python
# Example: Custom context manager for file operations
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Usage
with FileHandler('example.txt', 'w') as file:
    file.write('Hello, context manager!')
```

These advanced features in Python enhance code readability, conciseness, and functionality, making it easier to write clean and efficient code.