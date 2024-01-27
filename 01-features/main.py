import time

# Sample data: a text file with book titles and authors
with open('books.txt', 'w') as file:
    file.write("Python Programming by John Doe\n")
    file.write("Data Science Essentials by Jane Smith\n")
    file.write("Machine Learning Mastery by John Doe\n")
    file.write("Web Development Basics by Bob Johnson\n")
    file.write("Artificial Intelligence Fundamentals by Alice Brown\n")

# Decorator for timing
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.5f} seconds to execute.")
        return result
    return wrapper

# Context manager for reading file
class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Task 1: Extract titles of books written by John Doe using list comprehension
with FileReader('books.txt') as file:
    john_doe_books = [line.split('by')[0].strip() for line in file if 'John Doe' in line]

print("Books by John Doe:", john_doe_books)

# Task 2: Calculate average length of book titles using lambda function and generators
title_lengths = map(lambda title: len(title), john_doe_books)
average_length = sum(title_lengths) / len(john_doe_books)

print("Average length of titles:", average_length)

# Applying the timing decorator to the analysis function
@timing_decorator
def analyze_books():
    # Combine all the tasks in a function
    with FileReader('books.txt') as file:
        john_doe_books = [line.split('by')[0].strip() for line in file if 'John Doe' in line]
    title_lengths = map(lambda title: len(title), john_doe_books)
    average_length = sum(title_lengths) / len(john_doe_books)
    print("Books by John Doe:", john_doe_books)
    print("Average length of titles:", average_length)

# Task 3: Use the timing decorator to measure the execution time of the analysis
analyze_books()
