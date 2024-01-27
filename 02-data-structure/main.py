# Advanced Operations on Lists, Sets, and Dictionaries

# List Comprehension Example
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared Numbers:", squared_numbers)

# Slicing Example
original_list = [1, 2, 3, 4, 5]
sublist = original_list[2:5]
print("Sublist:", sublist)

# Set Comprehension Example
square_set = {x**2 for x in range(1, 6)}
print("Square Set:", square_set)

# Set Intersection Example
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection_result = set1 & set2
print("Intersection Result:", intersection_result)

# Dictionary Comprehension Example
square_dict = {x: x**2 for x in range(1, 6)}
print("Square Dictionary:", square_dict)

# Merging Dictionaries Example
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print("Merged Dictionary:", merged_dict)


# Explore More Complex Data Structures

# Queue Example
from queue import Queue

my_queue = Queue()
my_queue.put(1)
my_queue.put(2)
first_element = my_queue.get()
print("Queue Example - First Element:", first_element)

# Stack Example
my_stack = []
my_stack.append(1)
my_stack.append(2)
top_element = my_stack.pop()
print("Stack Example - Top Element:", top_element)

# Tree Example
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Tree Example
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print("Binary Tree Example - Root Value:", root.value)
