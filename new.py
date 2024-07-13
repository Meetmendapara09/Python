# Prints "Hello World!!" to the console
print("Hello World!!")

# Performs simple arithmetic operations on variables a and b
a = 1
b = 2
print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a % b)    # Modulo (remainder)
print(a // b)   # Floor division (integer division)

# Defines and calls a function func1 to print a string with an incremented number
def func1():
    number = 0
    number += 1
    print('Name' + str(number))

func1()
func1()
func1()

print("Function called 3 times.")

# Demonstrates string operations
message = "hello world"
print(len(message))         # Length of the string
print(message[2:5])         # Slicing: prints characters from index 2 to 4 (exclusive)

print(message.lower())      # Convert string to lowercase
print(message.upper())      # Convert string to uppercase
print(message.count('l'))   # Count occurrences of 'l' in the string
print(message.find('world'))    # Find index of 'world' in the string
print(message.find('hero'))     # Returns -1 if 'hero' is not found
print(message.replace('world', 'Meet'))  # Replace 'world' with 'Meet' in the string

name = 'Meet'
greetings = 'Hello'
wel_message = f'{greetings}, {name}. Welcome!'
print(wel_message)

# Demonstrates type and arithmetic operations
num = 3
print(type(num))    # Print type of variable num

num1 = 2.34
print(type(num1))   # Print type of variable num1

m1 = 5
m2 = 10
print(m1 + m2)      # Addition
print(m1 - m2)      # Subtraction
print(m1 * m2)      # Multiplication
print(m1 / m2)      # Division
print(m1 // m2)     # Floor division
print(m1 ** m2)     # Exponentiation
print(m1 % m2)      # Modulo

print(abs(-3))      # Absolute value
print(abs(10.4))

print(round(15.5))  # Round to nearest integer
print(round(15484.5486616645, 2))  # Round to 2 decimal places

# Demonstrates comparisons
val1 = 10
val2 = 20
print(val1 > val2)  # Greater than
print(val1 < val2)  # Less than
print(val1 == val2)  # Equal
print(val1 != val2)  # Not equal
print(val1 >= val2)  # Greater than or equal to
print(val1 <= val2)  # Less than or equal to

# Demonstrates string concatenation
num_1 = '1000'
num_2 = '2000'
print(num_1 + num_2)  # Concatenates strings num_1 and num_2

# Demonstrates type casting from string to integer
num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)  # Addition after type casting

# Demonstrates operations with lists
course = ['CSE', 'CE', 'IT', 'ECE', 'ICT']
print(course)           # Print entire list
print(course[2])        # Access element at index 2
print(len(course))      # Number of elements in the list
print(course[-1])       # Last element of the list
print(course[0:2])      # Elements from index 0 to 1 (exclusive)
print(course[2:])       # Elements from index 2 to end
print(course[:4])       # Elements from start to index 3 (exclusive)
print(course[::-1])     # Reverse the list

course.append('ME')     # Append 'ME' to the list
print(course)

course.remove('IT')     # Remove 'IT' from the list
print(course)

course.insert(2, 'EE')  # Insert 'EE' at index 2
print(course)

course.pop()            # Remove last element from the list
print(course)

course.reverse()        # Reverse the list
print(course)

course_no = [10, 2, 3, 4, 5]
course.insert(0, course_no)   # Insert course_no list at index 0
print(course)

print(course + course_no)       # Merge two lists without using built-in function
course.extend(course_no)        # Merge two lists using extend method
print(course)

course_no.sort()        # Sort elements of course_no list
print(course_no)

print(sum(course_no))   # Sum of elements in course_no list
print(max(course_no))   # Maximum value in course_no list
print(course.index('CSE'))     # Index of 'CSE' in course list
print('Arts' in course)        # Check if 'Arts' is in course list
print('CSE' in course)

# Demonstrates loops in Python
for item in course_no:
    print(item)         # Iterate and print each item in course_no list

for item, course_no in enumerate(course_no):
    print(item, course_no)  # Iterate and print index and item in course_no list

for item, course in enumerate([546, 7864, 546, 543], start=20):
    print(item, course)     # Iterate and print starting from index 20

cour = ['a', 'b', 'c', 'd']
course_str = ','.join(cour)     # Join elements of cour list with ',' and assign to course_str
print(course_str)

# Demonstrates tuple usage in Python
# Mutable list
list_1 = ['history', 'Math', 'Physics', 'Chemistry']
list_2 = list_1.copy()          # Copy list_1 to list_2

print(list_1)
print(list_2)

list_1[0] = 'Art'               # Modify list_1
print(list_1)
print(list_2)                   # list_2 remains unchanged

# Immutable tuple
tuple_1 = ('history', 'Math', 'Physics', 'Chemistry')
tuple_2 = tuple_1               # Assign tuple_1 to tuple_2

print(tuple_1)
print(tuple_2)

# We cannot modify tuple elements directly
# tuple_1[0] = 'Art'            # This will raise an error
# print(tuple_1)
# print(tuple_2)

# Sets in Python
cs_course = {'DSA', 'OOPS', 'COA', 'DBMS'}
bca_course = {'WEBD', 'OOPS', 'DBMS', 'SDE'}
print(cs_course)                # Print elements of cs_course set
print('COA' in cs_course)       # Check if 'COA' is in cs_course set
print(cs_course.intersection(bca_course))   # Intersection of cs_course and bca_course sets
print(cs_course.difference(bca_course))     # Difference of cs_course and bca_course sets
print(cs_course.union(bca_course))          # Union of cs_course and bca_course sets

# Empty Lists
empty_list = []
empty_list1 = list()

print(empty_list)               # Print empty_list
print(empty_list1)              # Print empty_list1

# Empty Tuples
empty_tuple = ()
empty_tuple1 = tuple()

print(empty_tuple)              # Print empty_tuple
print(empty_tuple1)             # Print empty_tuple1

# Empty Sets
empty_sets = {}                 # This is a dictionary, not an empty set
empty_sets1 = set()

print(empty_sets)               # Print empty_sets (empty dictionary)
print(empty_sets1)              # Print empty_sets1 (empty set)

# Dictionaries in Python
Student = {'name': 'Meet', 'age': '20', 'Courses': ['Math', 'CSE', 'Robotics']}
print(Student)                  # Print entire Student dictionary
print(Student['name'])          # Print value associated with 'name' key
print(Student.get('name'))      # Get value associated with 'name' key using get() method

# Get value with default message if key doesn't exist
print((Student.get('phone', 'Not Found')))

# Update value associated with 'age' key
Student['age'] = '21'
print(Student)

# Delete 'age' key-value pair from Student dictionary
del Student['age']
print(Student)

print(Student.keys())           # Print keys of Student dictionary
print(Student.values())         # Print values of Student dictionary
print(Student.items())          # Print key-value pairs of Student dictionary

# Iterate through keys of Student dictionary
for key in Student:
    print(key)

# Iterate through key-value pairs of Student dictionary
for key, value in Student.items():
    print(key, value)

# Conditionals and Booleans
if True:
    print("True Statement")     # Print if condition is True

if False:
    print("False Statement")    # Not printed if condition is False

a = 1000
b = 2000
c = a % b
if c == 0:
    print("number is rational")    # Print if condition is True
else:
    print("number is not rational")    # Print if condition is False

Language = ['Python', 'Java']
if 'Python' in Language:
    print('Language is Python')     # Print if 'Python' is in Language list
elif 'Java' in Language:
    print('Language is Java')       # Print if 'Java' is in Language list
else:
    print('No Match Found')         # Print if neither 'Python' nor 'Java' is in Language list

user = 'Admin'
logged_in = True

# Conditional checks with not, or, and
if not logged_in:
    print("Please Log in")
else:
    print("Welcome")

if user == 'Admin' or logged_in:
    print("Admin Page")             # Print if user is 'Admin' or logged_in is True
else:
    print("Bad Codes")              # Print if neither condition is met

if user == 'Admin' and logged_in:
    print("Admin Page")             # Print if user is 'Admin' and logged_in is True
else:
    print("Bad Codes")              # Print if either condition is not met

# Demonstrates use of break and continue in loops
a = [1, 2, 3]
b = a

print(id(a))                        # Print storage address of a
print(id(b))                        # Print storage address of b
print(id(a) == id(b))               # Print True if storage addresses of a and b are equal

for num in a:
    if num == 3:
        print("number founded!")
        break                       # Exit loop when num is 3
    print(num)

for num in a:
    if num == 3:
        print("number founded!")
        continue                    # Skip rest of loop and continue to next iteration when num is 3
    print(num)

for num in a:
    for letter in 'abcd':
        print(num, letter)          # Print num and each letter in 'abcd' for each num in a

for i in range(10):
    print(i)                        # Print numbers from 0 to 9

for i in range(5, 10):
    i += 1
    print(i)                        # Print numbers from 6 to 10

# While loop
x = 0
while x < 10:
    print(x)                        # Print values of x from 0 to 8 (incremented by 2 each iteration)
    x += 2

# Recursion
def hello_func(n):
    if n > 0:
        print("hello world")        # Print "hello world" n times recursively
        hello_func(n - 1)

hello_func(5)

# Function returning formatted string
def hello_function(greeting):
    return '{} Function.'.format(greeting)

print((hello_function('i\'m a test')))

# Function returning string
def sample():
    return 'hello Function.'

print(sample().upper())

# Function accepting variable number of arguments and keyword arguments
def student_info(*args, **kwargs):
    print(args)                     # Print positional arguments as tuple
    print(kwargs)                   # Print keyword arguments as dictionary

student_info('Math', 'Arts', name='Meet', age='20')

# Exception Handling
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
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
        print(line.strip())  # strip() removes any extra newline characters

# Handling file not found error
try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# Lambda Functions
square = lambda x: x ** 2
print(square(5))    # Output: 25

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)   # Output: [1, 4, 9, 16, 25]

# Sorting using lambda
students = [
    {'name': 'Alice', 'grade': 90},
    {'name': 'Bob', 'grade': 80},
    {'name': 'Charlie', 'grade': 95}
]
students.sort(key=lambda x: x['grade'], reverse=True)
print(students)   # Output: [{'name': 'Charlie', 'grade': 95}, {'name': 'Alice', 'grade': 90}, {'name': 'Bob', 'grade': 80}]

# List Comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)   # Output: [1, 4, 9, 16, 25]

# List comprehension with conditional
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)   # Output: [2, 4]

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_matrix = [num for row in matrix for num in row]
print(flattened_matrix)   # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Object-Oriented Programming (OOP)
class Dog:
    # Class variable
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old."

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Instantiate the Dog object
mikey = Dog("Mikey", 6)

# Access the instance attributes
print(mikey.description())  # Output: Mikey is 6 years old.

# Call an instance method
print(mikey.speak("Woof Woof"))  # Output: Mikey says Woof Woof

# Generators
def square_numbers(nums):
    for num in nums:
        yield num ** 2

numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(numbers)
print(list(squared_numbers))   # Output: [1, 4, 9, 16, 25]

# Decorators
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"Wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    print("Display function executed.")

display()   # Output: Wrapper executed this before display, Display function executed.

# Context Managers (with Statement)
class FileContextManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Using context manager
with FileContextManager('sample.txt', 'r') as file:
    contents = file.read()
    print(contents)

# JSON Handling
# Encode Python object to JSON
import json

student = {
    'name': 'John',
    'age': 22,
    'courses': ['Math', 'CompSci']
}
json_data = json.dumps(student, indent=2)  # Convert Python dict to JSON string with indentation
print(json_data)

# Decode JSON to Python object
json_string = '{"name": "Jane", "age": 25, "courses": ["Physics", "Chemistry"]}'
student_obj = json.loads(json_string)  # Convert JSON string to Python dict
print(student_obj)

# Working with Dates and Times
import datetime

# Current date and time
now = datetime.datetime.now()
print(now)

# Formatting date and time
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Parsing date from string
date_string = "2023-07-15 12:00:00"
parsed_date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(parsed_date)

# Regular Expressions
import re

text = "The rain in Spain"
matches = re.findall("ai", text)
print(matches)   # Output: ['ai', 'ai']

# Search and match
match = re.search(r"\bS\w+", text)
print(match.group())   # Output: Spain

# Substitute
new_text = re.sub(r"\bSpain\b", "Portugal", text)
print(new_text)   # Output: The rain in Portugal

# File Handling with os Module
import os
# Check if file exists
if os.path.exists("sample.txt"):
    print("File exists!")

# Get current working directory
current_directory = os.getcwd()
print(current_directory)

# List files and directories
files = os.listdir()
print(files)

# Working with CSV Files
import csv

# Writing to a CSV file
with open('data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 25])
    writer.writerow(['Bob', 30])

# Reading from a CSV file
with open('data.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Using argparse for Command-Line Arguments
import argparse

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))

# Multithreading
import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(0.1)

def print_letters():
    for letter in 'ABCDE':
        print(letter)
        time.sleep(0.1)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Waiting for threads to complete
thread1.join()
thread2.join()

print("Threads execution completed.")

# Virtual Environments and Packages
# Creating a virtual environment (command line)
# $ python -m venv myenv

# Activating the virtual environment (Windows)
# $ myenv\Scripts\activate

# Installing packages (example)
# $ pip install requests

# Using packages
import requests
response = requests.get('https://www.example.com')
print(response.status_code)

# Working with SQLite Database
import sqlite3

# Connecting to SQLite database
conn = sqlite3.connect('example.db')

# Creating a cursor object
cursor = conn.cursor()

# Executing SQL queries
cursor.execute('''CREATE TABLE IF NOT EXISTS students
                (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Inserting data into the table
cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 25)")

# Committing changes and closing connection
conn.commit()
conn.close()

# Web Scraping with BeautifulSoup
from bs4 import BeautifulSoup
import requests

# Fetching HTML content from a webpage
url = 'https://example.com'
response = requests.get(url)
html_content = response.text

# Parsing HTML with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extracting data from HTML
title = soup.title
print(title.text)   # Output: Example Domain

# Context Managers (with Statement)
# Using with statement to open and automatically close a file
with open('example.txt', 'w') as file:
    file.write('Hello, this is a sample text.')

# Custom context manager using class
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.execution_time = self.end_time - self.start_time
        print(f"Execution time: {self.execution_time} seconds")

# Using custom context manager
with Timer():
    time.sleep(2)  # Simulating some operation that takes time

# Decorators
# Creating a simple decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Applying decorator to a function
@my_decorator
def say_hello():
    print("Hello!")

say_hello()   # Output:
              # Something is happening before the function is called.
              # Hello!
              # Something is happening after the function is called.

# itertools Module
import itertools

# Using itertools.cycle()
cycle = itertools.cycle(['A', 'B', 'C'])
for _ in range(5):
    print(next(cycle))   # Output: A B C A B

# Using itertools.permutations()
perm = itertools.permutations([1, 2, 3])
print(list(perm))   # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# Threading and Multiprocessing
import threading
import multiprocessing

# Creating a thread
def thread_function():
    print("Thread is running...")

thread = threading.Thread(target=thread_function)
thread.start()

# Creating a process
def process_function():
    print("Process is running...")

process = multiprocessing.Process(target=process_function)
process.start()

# Asynchronous Programming (asyncio)
import asyncio

# Asynchronous coroutine function
async def greet():
    print("Hello,")
    await asyncio.sleep(1)   # Simulating asynchronous operation
    print("World!")

# Running asynchronous function
asyncio.run(greet())

# Unit Testing (unittest Module)
import unittest

# Example class to be tested
class MathOperations:
    def add(self, a, b):
        return a + b

# Unit test class
class TestMathOperations(unittest.TestCase):
    def setUp(self):
        self.math_operations = MathOperations()

    def test_add(self):
        result = self.math_operations.add(3, 5)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()

# Working with APIs (Requests Module)
import requests

# Making GET request to a public API
response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
data = response.json()

# Extracting data from API response
exchange_rate = data['rates']['EUR']
print(f"1 USD is equal to {exchange_rate} EUR")

# Contextlib Module (Context Managers)
from contextlib import contextmanager

# Custom context manager using contextlib
@contextmanager
def file_manager(filename, mode):
    try:
        file = open(filename, mode)
        yield file
    finally:
        file.close()

# Using custom context manager
with file_manager('example.txt', 'w') as file:
    file.write('Hello, this is a contextlib example.')

# Data Classes (dataclasses Module)
from dataclasses import dataclass

# Creating a data class
@dataclass
class Student:
    name: str
    age: int
    courses: list

# Creating an instance of the data class
student = Student("Carol", 21, ["Chemistry", "Geography"])
print(student.name, student.age, student.courses)

# Logging (logging Module)
import logging

# Configuring logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Using logging
logging.info('This is an information message.')
logging.warning('This is a warning message.')
