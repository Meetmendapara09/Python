# hello world

print("Hello World!!")

# simple math work
a = 1
b = 2
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a // b)


# function


def func1():
    number = 0
    number += 1
    print('Name' + str(number))


func1()
func1()
func1()

print("Function called 3 times.")

# length of word

message = "hello world"
print(len(message))
print(message[2:5])

# lower case - upper case

print(message.lower())   # to convert the string into lower case
print(message.upper())   # to convert the string into the upper case
print(message.count('l'))  # how many times that word or letter being used
print(message.find('world'))  # if the word is available then it returns the index of the words
print(message.find('hero'))   # otherwise it returns the -1 value
print(message.replace('world', 'Meet'))

name = 'Meet'
greetings = 'Hello'

wel_message = f'{greetings}, {name}. Welcome!'

print(wel_message)


# type of the variable
num = 3

print(type(num))

num1 = 2.34

print(type(num1))

# arithmetic operation

m1 = 5
m2 = 10

print(m1 + m2)  # addition
print(m1 - m2)  # subtraction
print(m1 * m2)  # multiplication
print(m1 / m2)  # division
print(m1 // m2)  # floor division
print(m1 ** m2)  # exponent
print(m1 % m2)  # modulo

# absolute value
print(abs(-3))
print(abs(10.4))

# round of the value
print(round(15.5))
print(round(15484.5486616645, 2))  # round of the value at precise decimal

# comparisons

val1 = 10
val2 = 20

print(val1 > val2)  # greater then
print(val1 < val2)  # less than
print(val1 == val2)  # equal
print(val1 != val2)  # not equal
print(val1 >= val2)  # greater than or equal to
print(val1 <= val2)  # less than or equal to

# string addition

num_1 = '1000'
num_2 = '2000'

print(num_1 + num_2)

# type casting
# string to integer
num_1 = int(num_1)
num_2 = int(num_2)

print(num_1 + num_2)

# list :- A list in Python is a comma-separated collection of expressions enclosed in square brackets.

course = ['CSE', 'CE', 'IT', 'ECE', 'ICT']

print(course)   # To print the whole list
print(course[2])  # it will return the 2nd element of the list
print(len(course))  # returns the number of element
print(course[-1])   # returns the value from the last
print(course[0:2])  # returns the interval elements
print(course[2:])   # returns the values from starting positions
print(course[:4])   # returns the elements till the end positions
print(course[::-1])  # to return the full list in reverse order

course.append('ME')  # to remove the element into the list
print(course)

course.remove('IT')   # to remove the element from the list
print(course)

course.insert(2, 'EE')  # to insert the element in specific position
print(course)

course.pop()  # delete the last element in the list
print(course)

course.reverse()  # to reverse the list
print(course)

course_no = [10, 2, 3, 4, 5]
course.insert(0, course_no)   # to insert the new list into the existing list from specific positions
print(course)


# to merge the two list without inbuilt functions
print(course + course_no)

# to merge the two list with inbuilt function
course.extend(course_no)
print(course)

# to sort the list elements
course_no.sort()
print(course_no)

print(sum(course_no))
print(max(course_no))
print(course.index('CSE'))
print('Arts' in course)   # returns true if available in the list otherwise false
print('CSE' in course)


# Loop in Python

# for loop in python :- print the all element in the list
for item in course_no:
    print(item)

for item, course_no in enumerate(course_no):
    print(item, course_no)

# for assigning the index starting value to the list to iterate
for item, course in enumerate([546, 7864, 546, 543], start=20):
    print(item, course)


# join function in python to join the values
cour = ['a', 'b', 'c', 'd']
course_str = ','.join(cour)
print(course_str)


# Tuple :- it is similar to List but there is one difference that List are Mutable  but Tuple is immutable.

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

# we can't add, delete or remove the values into the tuple , if we do it returns the error message
# tuple_1[0] = 'Art'
#
# print(tuple_1)
# print(tuple_2)


# Sets in Python :- writes in {}
# Sets :- it can't return the same index as we deliver to the system.

cs_course = {'DSA', 'OOPS', 'COA', 'DBMS'}
bca_course = {'WEBD', 'OOPS', 'DBMS', 'SDE'}
print(cs_course)
print('COA' in cs_course)  # check the value is either in the set or not
print(cs_course.intersection(bca_course))   # intersection from 2 sets A ∩ B
print(cs_course.difference(bca_course))     # difference from 2 sets A - B
print(cs_course.union(bca_course))          # union of sets A ∪ B


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

empty_sets = {}  # this isn't right! It's a dictionary
empty_sets1 = set()

print(empty_sets)
print(empty_sets1)

# Dictionary :- It's like hashmap.

Student = {'name': 'Meet', 'age': '20', 'Courses': ['Math', 'CSE', 'Robotics']}

print(Student)      # it will print the whole Dictionary.
print(Student['name'])      # in [] if we pass the required parameters then it only returns that parameter
print(Student.get('name'))  # get() to get the required data from Dictionary

# it will act like an access key to getting the data from the Dictionary
# if the value is found , it returns the value otherwise it returns our message

print((Student.get('phone', 'Not Found')))
Student['phone'] = '123456789'
print((Student.get('phone', 'Not Found')))


# to update the value in the Dictionary
Student.update({'age': '21'})
print(Student)

# del function to delete the data from Dictionary
del Student['age']
print(Student)

# print the keys of the Dictionary
# and in the Dictionary the key means the parameters like name, age , phone number
print(Student.keys())
print(Student.values())
# the .values functions is responsible to returns the values of the parameter

# item function is used to get the Dictionary data with their id and data
print(Student.items())

for key in Student:
    print(key)

for Key, value in Student.items():
    print(Key, value)

# Conditionals and Booleans - if , else , elif

if True:
    print("True Statement")

if False:
    print("False Statement")

a = 1000
b = 2000
c = a % b
if c == 0:
    print("number is rational")
else:
    print("number is not rational")

# Comparisons:
# Equal             :  ==
# #Not Equal        :  !=
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

print(id(a))  # id means the storage address or any other garbage value
print(id(b))
print(id(a) == id(b))


a = [1, 2, 3, 4, 5]

# break is breaking the loop
for num in a:
    if num == 3:
        print("number founded!")
        break
    print(num)

# continue is print the message and continue the loop to iterate
for num in a:
    if num == 3:
        print("number founded!")
        continue
    print(num)

# here in this code snippet the value is assigned a character and print number and character until the last number
# last character is not print. like 5 d in this code
for num in a:
    for letter in 'abcd':
        print(num, letter)

for i in range(10):
    print(i)

for i in range(5, 10):
    i += 1
    print(i)

# while loop
x = 0
while x < 10:
    print(x)
    x += 2

# recursion


def hello_func(n):
    if n > 0:
        print("hello world")
        hello_func(n - 1)


hello_func(5)


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
