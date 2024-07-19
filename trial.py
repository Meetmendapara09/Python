# Comments
# Hello World
print("Hello World!!")

# Simple math operations
a = 1
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)

# Function
def func1():
    number = 0
    number += 1
    print('Name' + str(number))

func1()
func1()
func1()

print("Function called 3 times.")

# Length of string
message = "hello world"
print(len(message))
print(message[2:5])

# Lowercase - Uppercase
print(message.lower())   # Convert string to lowercase
print(message.upper())   # Convert string to uppercase
print(message.count('l'))  # Count occurrences of 'l'
print(message.find('world'))  # Find index of 'world'
print(message.find('hero'))   # Find returns -1 if not found
print(message.replace('world', 'Meet'))

name = 'Meet'
greetings = 'Hello'

wel_message = f'{greetings}, {name}. Welcome!'

print(wel_message)

# Type of variables
num = 3
print(type(num))

num1 = 2.34
print(type(num1))

# Arithmetic operations
m1 = 5
m2 = 10
print(m1 + m2)  # Addition
print(m1 - m2)  # Subtraction
print(m1 * m2)  # Multiplication
print(m1 / m2)  # Division
print(m1 // m2)  # Floor division
print(m1 ** m2)  # Exponent
print(m1 % m2)  # Modulo

# Absolute value
print(abs(-3))
print(abs(10.4))

# Round of the value
print(round(15.5))
print(round(15484.5486616645, 2))  # Round to 2 decimal places

# Comparisons
val1 = 10
val2 = 20
print(val1 > val2)  # Greater than
print(val1 < val2)  # Less than
print(val1 == val2)  # Equal
print(val1 != val2)  # Not equal
print(val1 >= val2)  # Greater than or equal to
print(val1 <= val2)  # Less than or equal to

# String addition
num_1 = '1000'
num_2 = '2000'
print(num_1 + num_2)

# Type casting
# String to integer
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)

# List
course = ['CSE', 'CE', 'IT', 'ECE', 'ICT']
print(course)   # Print the whole list
print(course[2])  # Access the 2nd element
print(len(course))  # Length of the list
print(course[-1])   # Last element
print(course[0:2])  # Slice elements
print(course[2:])   # Elements from index 2
print(course[:4])   # Elements till index 4
print(course[::-1])  # Reverse the list
course.append('ME')  # Append 'ME' to the list
print(course)
course.remove('IT')   # Remove 'IT' from the list
print(course)
course.insert(2, 'EE')  # Insert 'EE' at index 2
print(course)
course.pop()  # Delete the last element
print(course)
course.reverse()  # Reverse the list
print(course)
course_no = [10, 2, 3, 4, 5]
course.insert(0, course_no)   # Insert course_no list into course at index 0
print(course)
# Merge two lists without using inbuilt functions
print(course + course_no)
# Merge two lists using inbuilt function
course.extend(course_no)
print(course)
# Sort the list elements
course_no.sort()
print(course_no)
print(sum(course_no))
print(max(course_no))
print(course.index('CSE'))
print('Arts' in course)   # Check if 'Arts' is in the list
print('CSE' in course)

# Loop in Python
# For loop to print all elements in the list
for item in course_no:
    print(item)
# Enumerate to get index and value
for item, course_no in enumerate(course_no):
    print(item, course_no)
# Assigning index starting value to iterate over a list
for item, course in enumerate([546, 7864, 546, 543], start=20):
    print(item, course)

# Join function to join list elements into a string
cour = ['a', 'b', 'c', 'd']
course_str = ','.join(cour)
print(course_str)

# Tuple
# Mutable
list_1 = ['history', 'Math', 'Physics', 'Chemistry']
list_2 = list_1
print(list_1)
print(list_2)
list_1[0] = 'Art'
print(list_1)
print(list_2)
# Immutable
tuple_1 = ('history', 'Math', 'Physics', 'Chemistry')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# Sets in Python
cs_course = {'DSA', 'OOPS', 'COA', 'DBMS'}
bca_course = {'WEBD', 'OOPS', 'DBMS', 'SDE'}
print(cs_course)
print('COA' in cs_course)  # Check if 'COA' is in cs_course
print(cs_course.intersection(bca_course))   # Intersection of cs_course and bca_course
print(cs_course.difference(bca_course))     # Difference of cs_course and bca_course
print(cs_course.union(bca_course))          # Union of cs_course and bca_course

# Empty Lists
empty_list = []
empty_list1 = list()
print(empty_list)
print(empty_list1)

# Empty Tuple
empty_tuple = ()
empty_tuple1 = tuple()
print(empty_tuple)
print(empty_tuple1)

# Empty Sets
empty_sets = set()
print(empty_sets)

# Dictionary
Student = {'name': 'Meet', 'age': '20', 'Courses': ['Math', 'CSE', 'Robotics']}
print(Student)      # Print the whole dictionary
print(Student['name'])      # Access 'name'
print(Student.get('name'))  # Get 'name'
print(Student.get('phone', 'Not Found'))  # Get 'phone' or 'Not Found'
Student['phone'] = '123456789'  # Update 'phone'
print(Student.get('phone', 'Not Found'))
Student.update({'age': '21'})  # Update 'age'
print(Student)
del Student['age']  # Delete 'age'
print(Student)
print(Student.keys())  # Print keys
print(Student.values())  # Print values
print(Student.items())  # Print items
for key in Student:  # Iterate over keys
    print(key)
for key, value in Student.items():  # Iterate over items
    print(key, value)

# Conditionals and Booleans
if True:
    print("True Statement")
if False:
    print("False Statement")
a = 1000
b = 2000
c = a % b
if c == 0:
    print("Number is rational")
else:
    print("Number is not rational")
# Comparisons:
# Equal             :  ==
# Not Equal         :  !=
# Greater Than      :  >
# Less Than         :  <
# Greater or Equal  :  >=
# Less or Equals    :  <=
# Object Identity   :  is
Language = ['Python', 'Java']
if 'Python' in Language:
    print('Language is Python')
elif 'Java' in Language:
    print('Language is Java')
else:
    print('No Match Found')
user = 'Admin'
logged_in = True
# not method
if not logged_in:
    print("Please Log in")
else:
    print("Welcome")
# or method
if user == 'Admin' or logged_in:
    print("Admin Page")
else:
    print("Bad Codes")
# and method
if user == 'Admin' and logged_in:
    print("Admin Page")
else:
    print("Bad Codes")
a = [1, 2, 3]
b = a
print(id(a))  # Memory address of 'a'
print(id(b))  # Memory address of 'b'
print(id(a) == id(b))

a = [1, 2, 3, 4, 5]
# break to terminate loop
for num in a:
    if num == 3:
        print("Number found!")
        break
    print(num)
# continue to move the loop
for num in a:
    if num == 3:
        print("Number found!")
        continue
    print(num)
# This code snippet assigns a value to a number and prints it until the final number is printed, like 5 d in this code
for num in a:
    for letter in 'abcd':
        print(num, letter)

for i in range(10):
    print(i)

for i in range(5, 10):
    i += 1
    print(i)

# While loop to print x values
x = 0
while x < 10:
    print(x)
    x += 2

# Recursion function
def hello_func(n):
    if n > 0:
        print("hello world")
        hello_func(n - 1)

hello_func(5)

# Custom function
def hello_function(greeting):
    return '{} Function.'.format(greeting)

print((hello_function('i\'m a test')))

def sample():
    return 'hello Function.'

print(sample().upper())

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Arts', name='Meet', age='20')

# Exception Handling
try:
    result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division successful!")
finally:
    print("Execution complete.")

# Handling specific exceptions
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"Your number is: {num}")
finally:
    print("Input handling complete.")

# File Operations
# Writing to a file
with open('sample.txt', 'w') as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Writing some more lines.")

# Reading from a file
with open('sample.txt', 'r') as file:
    contents = file.read()
    print(contents)

# Appending to a file
with open('sample.txt', 'a') as file:
    file.write("\nAppending a new line to the file.")

# Reading line by line
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # Remove any extra newline characters

# Handling file not found error
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# Additional Concepts

# Classes and Object-Oriented Programming (OOP)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks.")

dog = Dog("Buddy")
dog.speak()

# Lambda Functions
addition = lambda x, y: x + y
print(addition(2, 3))

# Generators and Iterators
def generator_example():
    for i in range(5):
        yield i

gen = generator_example()
for value in gen:
    print(value)

# Decorators
def decorator_func(original_func):
    def wrapper_func():
        print("Wrapper executed this before {}".format(original_func.__name__))
        return original_func()
    return wrapper_func

@decorator_func
def display():
    print("Display function executed.")

display()

# Modules and Packages
import math
print(math.sqrt(16))

# Concurrency and Threading
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# Assertions
x = 10
y = 0
assert y != 0, "Divide by zero error"
print(x / y)

# Context Managers
class FileHandler:
    def __enter__(self):
        print("Entering context...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context...")

with FileHandler() as fh:
    print("Inside the context.")

# Regular Expressions
import re

pattern = r'\b\d{3}\b'
text = "123 4567 890 12345"
matches = re.findall(pattern, text)
print(matches)

# Functional Programming (map, filter, reduce)
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(squared)
print(evens)
print(product)

# Data Structures (collections module)
from collections import deque, defaultdict, namedtuple

# Example usage of deque, defaultdict, namedtuple

# Concepts not covered in the previous code snippet

# 1. List comprehensions
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
print(squared)
print(evens)

# 2. Dictionary comprehensions
numbers_dict = {x: x ** 2 for x in numbers}
print(numbers_dict)

# 3. Set comprehensions
numbers_set = {x for x in numbers}
print(numbers_set)

# 4. File handling (Using 'with' statement)
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# 5. Error handling with try-except-else-finally block
try:
    result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division successful!")
finally:
    print("Execution complete.")

# 6. Handling specific exceptions
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"Your number is: {num}")
finally:
    print("Input handling complete.")

# 7. Lambda functions
addition = lambda x, y: x + y
print(addition(2, 3))

# 8. Generators and Iterators
def generator_example():
    for i in range(5):
        yield i

gen = generator_example()
for value in gen:
    print(value)

# 9. Decorators
def decorator_func(original_func):
    def wrapper_func():
        print("Wrapper executed this before {}".format(original_func.__name__))
        return original_func()
    return wrapper_func

@decorator_func
def display():
    print("Display function executed.")

display()

# 10. Modules and Packages
import math
print(math.sqrt(16))

# 11. Concurrency and Threading
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# 12. Assertions
x = 10
y = 0
assert y != 0, "Divide by zero error"
print(x / y)

# 13. Context Managers
class FileHandler:
    def __enter__(self):
        print("Entering context...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context...")

with FileHandler() as fh:
    print("Inside the context.")

# 14. Regular Expressions
import re

pattern = r'\b\d{3}\b'
text = "123 4567 890 12345"
matches = re.findall(pattern, text)
print(matches)

# 15. Functional Programming (map, filter, reduce)
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

# 16. Data Structures (collections module)
from collections import deque, defaultdict, namedtuple

# Example usage of deque, defaultdict, namedtuple
queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
print(queue)

default_dict = defaultdict(int)
default_dict['key1'] = 1
print(default_dict['key1'])
print(default_dict['key2'])

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
# Concepts not covered in the previous code snippet (continued)

# 17. List comprehensions
numbers = [1, 2, 3, 4, 5]
squared = [x ** 2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
print(squared)
print(evens)

# 18. Dictionary comprehensions
numbers_dict = {x: x ** 2 for x in numbers}
print(numbers_dict)

# 19. Set comprehensions
numbers_set = {x for x in numbers}
print(numbers_set)

# 20. File handling (Using 'with' statement)
with open('sample.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

# 21. Error handling with try-except-else-finally block
try:
    result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Division successful!")
finally:
    print("Execution complete.")

# 22. Handling specific exceptions
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"Your number is: {num}")
finally:
    print("Input handling complete.")

# 23. Lambda functions
addition = lambda x, y: x + y
print(addition(2, 3))

# 24. Generators and Iterators
def generator_example():
    for i in range(5):
        yield i

gen = generator_example()
for value in gen:
    print(value)

# 25. Decorators
def decorator_func(original_func):
    def wrapper_func():
        print("Wrapper executed this before {}".format(original_func.__name__))
        return original_func()
    return wrapper_func

@decorator_func
def display():
    print("Display function executed.")

display()

# 26. Modules and Packages
import math
print(math.sqrt(16))

# 27. Concurrency and Threading
import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

thread = threading.Thread(target=print_numbers)
thread.start()
thread.join()

# 28. Assertions
x = 10
y = 0
assert y != 0, "Divide by zero error"
print(x / y)

# 29. Context Managers
class FileHandler:
    def __enter__(self):
        print("Entering context...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context...")

with FileHandler() as fh:
    print("Inside the context.")

# 30. Regular Expressions
import re

pattern = r'\b\d{3}\b'
text = "123 4567 890 12345"
matches = re.findall(pattern, text)
print(matches)

# 31. Functional Programming (map, filter, reduce)
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)

# 32. Data Structures (collections module)
from collections import deque, defaultdict, namedtuple

# Example usage of deque, defaultdict, namedtuple
queue = deque([1, 2, 3])
queue.append(4)
queue.popleft()
print(queue)

default_dict = defaultdict(int)
default_dict['key1'] = 1
print(default_dict['key1'])
print(default_dict['key2'])

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
