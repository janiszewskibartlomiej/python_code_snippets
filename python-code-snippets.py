## Taking Two Integers as input
a,b = map(int,input("podaj dwie liczby odzielone spacja: ").split())
print("a:",a)
print("b:",b)

## Taking a List as input
arr = list(map(int,input("podaj dwie liczby odzielone spacja: ").split()))
print("Input List:",arr)

# Enumerate
arr = [2,4,6,3,8,10]

for index,value in enumerate(arr):
  print(f"At Index {index} The Value Is -> {value}")

#  Check Memory Usage
import sys

arr = [2,4,6,3,8,10]

a = 20

print(sys.getsizeof(a))
print(sys.getsizeof(arr))

# Prints the Unique ID of a Variable

print(id(a))
print(id(arr))

# Check for an Anagram


def check_anagram(first_word, second_word):
  return sorted(first_word) == sorted(second_word)


print(check_anagram("silent", "listen"))  # True
print(check_anagram("ginger", "danger"))  # False

# Merging Two Dictionaries

basic_information = {"name":['karl','Lary'],"mobile":["0134567894","0123456789"]}
academic_information = {"grade":["A","B"]}
details = dict() ## Combines Dict

index = 1
for data in (basic_information, academic_information):
  print("index: ", index, "data: ", data)
  index += 1
  for key, value in data.items():
    print("key >> ", key, " Value >> ", value)
    print("data items >> ", data.items())

## Dictionary Comprehension Method
details = {key: value
           for data in (basic_information, academic_information)
           for key,value in data.items()}
print(details)

## Dictionary unpacking
details = {**basic_information ,**academic_information}
print(details)

## Copy and Update Method
details = basic_information.copy()
details.update(academic_information)
print(details)

# Checking if a File Exists

# Brute force Method
import os.path
from os import path


def check_for_file():
  print("File exists: ", path.exists("data.txt"))


check_for_file()

# Square of all numbers in a given range

# METHOD 1
from itertools import repeat

n = 5
squares = list(map(pow, range(1, n+1), repeat(2)))
print(squares)

# METHOD 2
n1 = 6
squares = [i**2 for i in range(1, n1+1)]
print(squares)


"""Output
  [1, 4, 9, 16, 25]
"""

# Converting two lists into a dictionary

list1 = ['karl','lary','keera']
list2 = [28934,28935,28936]

# Method 1: zip()
dictt0 = dict(zip(list1,list2))
print(dictt0)

# Method 2: dictionary comprehension
dictt1 = {key:value for key,value in zip(list1,list2)}
print(dictt1)

# Method 3: Using a For Loop (Not Recommended)
tuples = zip(list1, list2)
print(tuples)

dictt2 = {}
for key, value in tuples:
  print(key, value)
  if key in dictt2:
    pass
  else:
    dictt2[key] = value
print(dictt0, dictt1, dictt2, sep = "\n")

#  Sorting a List of Strings

list1 = ["Karl","Larry","Ana","Zack"]
print(list1)

# Method 1: sort()
list1.sort()
print(list1)

# Method 2: sorted()
sorted_list = sorted(list1, reverse=True)
print(sorted_list)

# Method 3: Brute Force Method
size = len(list1)
for i in range(size):
  for j in range(size):
    if list1[i] < list1[j]:
       temp = list1[i]
       list1[i] = list1[j]
       list1[j] = temp
print(list1)

# List Comprehension With if and Else

# new_list = [expression for member in iterable (if conditional)]

# new_list = [expression (if conditional) for member in iterable]

original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
prices = [i if i > 0 else 0 for i in original_prices]
# [1.25, 0, 10.22, 3.78, 0, 1.16]

def get_price(price):
    return price if price > 0 else 0
prices = [get_price(i) for i in original_prices]
# [1.25, 0, 10.22, 3.78, 0, 1.16]

# Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]

print(matrix)

# using lambda to print table of 10
numbers = list(map(lambda i: i*10, [i for i in range(1,6)]))

print(numbers)

# Assign matrix
twoDMatrix = [[10, 20, 30],
			[40, 50, 60],
			[70, 80, 90]]

# Generate transpose
trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix))]

print(trans)

# Python program to find second largest
# number in a list

# list of numbers - length of
# list should be at least 2
list1 = [10, 20, 4, 45, 99]

mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
	if list1[i]>mx:
		secondmax=mx
		mx=list1[i]
	elif list1[i]>secondmax and \
		mx != list1[i]:
		secondmax=list1[i]

print("Second highest number is : ",\
	str(secondmax))


# Adding Elements of Two Lists

maths = [59, 64, 75, 86]
physics = [78, 98, 56, 56]

# Brute Force Method
list1 = [
  maths[0]+physics[0],
  maths[1]+physics[1],
  maths[2]+physics[2],
  maths[3]+physics[3]
]


# List Comprehension
list1 = [x + y for x,y in zip(maths,physics)]

# Using Maps
import operator
all_devices = list(map(operator.add, maths, physics))

# Using Numpy Library
import numpy as np
list1 = np.add(maths,physics)

'''Output
[137 162 131 142]
'''

# Sorting a List of Dictionaries

dict1 = [
    {"Name":"Karl",
     "Age":25},
     {"Name":"Lary",
     "Age":39},
     {"Name":"Nina",
     "Age":35}
]

## Using sort()
dict1.sort(key=lambda item: item.get("Age"))
print(dict1)

# List sorting using itemgetter
from operator import itemgetter
f = itemgetter('Name')
dict1.sort(key=f)


# Iterable sorted function
dict1 = sorted(dict1, key=lambda item: item.get("Age"))

'''Output
[{'Age': 25, 'Name': 'Karl'},
 {'Age': 35, 'Name': 'Nina'},
 {'Age': 39, 'Name': 'Lary'}]
'''

# Calculating Time of a Shell

# METHOD 1
import datetime
start = datetime.datetime.now()
"""
CODE
"""
print(datetime.datetime.now()-start)

# METHOD 2
import time
start_time = time.time()
print(f"Total Time To Execute The Code is {(time.time() - start_time)}" )

# METHOD 3
import timeit
code = '''
## Code snippet whose execution time is to be measured
[2,6,3,6,7,1,5,72,1].sort()
'''
print(timeit.timeit(stmy = code,number = 1000))



# Checking For Substrings In a String of List


addresses = [
  "12/45 Elm street",
  '34/56 Clark street',
  '56,77 maple street',
  '17/45 Elm street'

]
street = 'Elm street'
for i in addresses:
  if street in i:
    print(i)

'''output
12/45 Elm street
17/45 Elm street
'''

#  Formatting a String

name = "Abhay"
age = 21

## METHOD 1: Concatenation
print("My name is "+name+", and I am "+str(age)+ " years old.")

## METHOD 2: F-strings (Python 3+)
print(f"My name is {name}, and I am {age} years old")

## METHOD 3: Join
print(''.join(["My name is ", name, ", and I am ", str(age), " years old"]))

## METHOD 4: modulus operator
print("My name is %s, and I am %d years old." % (name, age))

## METHOD 5: format(Python 2 and 3)
print("My name is {}, and I am {} years old".format(name, age))

# Error Handling

# Example 1
try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a / b
    print(c)
except:
    print("Can't divide with zero")

# Example 2
try:
    # this will throw an exception if the file doesn't exist.
    fileptr = open("file.txt", "r")
except IOError:
    print("File not found")
else:
    print("The file opened successfully")
    fileptr.close()

# Example 3
try:
    fptr = open("data.txt", 'r')
    try:
        fptr.write("Hello World!")
    finally:
        fptr.close()
        print("File Closed")
except:
    print("Error")

#  Calculator Without if-else

import operator

action = {
  "+" : operator.add,
  "-" : operator.sub,
  "/" : operator.truediv,
  "*" : operator.mul,
  "**" : pow
}

print(action['*'](5, 5))    # 25

# Chained function call


def add(a,b):
  return a+b

def sub(a,b):
  return a-b

a,b = 9,6
print((sub if a > b else add)(a, b))

#  Swap Values

a,b = 5,7

# Method 1
b,a = a,b

# Method 2
def swap(a,b):
  return b,a
swap(a,b)

# Flatten
# The following methods flatten a potentially deep list using recursion.


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret

def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list


deep_flatten([1, [2], [[3], 4], 5]) # [1,2,3,4,5]

# Difference
# This method finds the difference between two iterables by keeping only the values that are in the first one.


def difference(a, b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return list(comparison)


difference([1,2,3], [1,2,4]) # [3]

# Difference by
# The following method returns the difference between two lists after applying a given function to each element of both lists.

def difference_by(a, b, fn):
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


from math import floor
difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x']) # [ { x: 2 } ]

# Chained function call

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

a, b = 4, 5
print((subtract if a > b else add)(a, b)) # 9

#  Has duplicates

def has_duplicates(lst):
    return len(lst) != len(set(lst))


x = [1, 2, 3, 4, 5, 5]
y = [1, 2, 3, 4, 5]
has_duplicates(x)  # True
has_duplicates(y)  # False

# converting string

def palindrome(a):
    return a == a[::-1]


palindrome('mom') # True

# Get default value for missing keys

d = {'a': 1, 'b': 2}

print(d.get('c', 3))

"""
do przerobienia:

3. https://www.30secondsofcode.org/python/s/count-by

https://therenegadecoder.com/code/python-code-snippets-for-everyday-problems/
"""

# Inverting a Dictionary
# Sometimes when we have a dictionary, we want to be able to flip its keys and values. Of course, there are concerns like “how do we deal with duplicate values?” and “what if the values aren’t hashable?” That said, in the simple case, there are a few solutions:

my_dict = {
  'Izuku Midoriya': 'One for All',
  'Katsuki Bakugo': 'Explosion',
  'All Might': 'One for All',
  'Ochaco Uraraka': 'Zero Gravity'
}
# Use to invert dictionaries that have unique values
my_inverted_dict = dict(map(reversed, my_dict.items()))
print(my_inverted_dict)
print(map(reversed, my_dict.items()))
# Use to invert dictionaries that have unique values
my_inverted_dict = {value: key for key, value in my_dict.items()}
# Use to invert dictionaries that have non-unique values
from collections import defaultdict
my_inverted_dict = defaultdict(list)
{my_inverted_dict[v].append(k) for k, v in my_dict.items()}
# Use to invert dictionaries that have non-unique values
my_inverted_dict = dict()
for key, value in my_dict.items():
    my_inverted_dict.setdefault(value, list()).append(key)
# Use to invert dictionaries that have lists of values
my_dict = {value: key for key in my_inverted_dict for value in my_inverted_dict[key]}

# Performing a Reverse Dictionary Lookup
# Earlier we talked about reversing a dictionary which is fine in some circumstances. Of course, if our dictionary is enormous, it might not make sense to outright flip the dict. Instead, we can lookup a key based on a value:

my_dict = {"color": "red", "width": 17, "height": 19}
value_to_find = "red"
# Brute force solution (fastest) -- single key
for key, value in my_dict.items():
    if value == value_to_find:
        print(f'{key}: {value}')
        break
# Brute force solution -- multiple keys
for key, value in my_dict.items():
    if value == value_to_find:
        print(f'{key}: {value}')
# Generator expression -- single key
key = next(key for key, value in my_dict.items() if value == value_to_find)
print(f'{key}: {value_to_find}')
# Generator expression -- multiple keys
exp = (key for key, value in my_dict.items() if value == value_to_find)
for key in exp:
    print(f'{key}: {value}')
# Inverse dictionary solution -- single key
my_inverted_dict = {value: key for key, value in my_dict.items()}
print(f'{my_inverted_dict[value_to_find]}: {value_to_find}')
# Inverse dictionary solution (slowest) -- multiple keys
my_inverted_dict = dict()
for key, value in my_dict.items():
    my_inverted_dict.setdefault(value, list()).append(key)
print(f'{my_inverted_dict[value_to_find]}: {value_to_find}')

# Print data in one line

print("Mob Psycho 100", end="")
print("Mob Psycho 100", end="")
print("Mob Psycho 100", end="")

# Calculate execution Time
# This snippet is useful for you when you want to know how much time your program or a function takes to complete its execution.
import time
start_time= time.time()
def fun():
    a=2
    b=3
    c=a+b
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken)

# Sorting Dictionary
# This snippet will be used to sort the dictionary. check out the following code to know how it works.
orders = {
 'pizza': 200,
 'burger': 56,
 'pepsi': 25,
    'Coffee': 14
}
sorted_dic= sorted(orders.items(), key=lambda x: x[1])
print(sorted_dic)
print(orders.items())

# Retrieving the Last Element of the List
# This snippet will show how to retrieve the last element of the list.
my_list = ["Python", "JavaScript", "C++", "Java", "C#", "Dart"]
#method 1
print(my_list[-1])  # Dart
#method 2
print(my_list.pop())

# Shuffle a list
# This snippet code will show you how to shuffle a list in an easy and fast way.
from random import shuffle
my_list1=[1,2,3,4,5,6]
my_list2=["A","B","C","D"]
shuffle(my_list1) # [4, 6, 1, 3, 2, 5]
shuffle(my_list2) # ['A', 'D', 'B', 'C']

# finding frequency of each element in a list
from collections import Counter

my_list = ['a','a','b','b','b','c','d','d','d','d','d']
count = Counter(my_list) # defining a counter object

print(count) # Of all elements
# Counter({'d': 5, 'b': 3, 'a': 2, 'c': 1})

x = (dict(count))
print(x)

print(count['b']) # of individual element
# 3

print(count.most_common(1)) # most frequent element
# [('d', 5)]

#  Flattening a List of Lists
# Sometimes you’re not sure about the nesting depth of your list, and you simply want all the elements in a single flat list.

# pip3 install iteration-utilities
from iteration_utilities import deepflatten

# if you only have one depth nested_list, use this
def flatten(l):
  return [item for sublist in l for item in sublist]

l = [[1,2,3],[3]]
print(flatten(l))
# [1, 2, 3, 3]

# if you don't know how deep the list is nested
l = [[1,2,3],[4,[5],[6,7]],[8,[9,[10]]]]

print(list(deepflatten(l, depth=3)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Sampling From a List
# The following snippet generates n number of random samples from a given list using the random library.


import random

my_list = ['a', 'b', 'c', 'd', 'e']
num_samples = 2

samples = random.sample(my_list,num_samples)
print(samples)
# [ 'a', 'e'] this will have any 2 random values


import secrets                              # imports secure module.
secure_random = secrets.SystemRandom()      # creates a secure random object.

my_list = ['a','b','c','d','e']
num_samples = 2

samples = secure_random.sample(my_list, num_samples)

print(samples)
# [ 'e', 'd'] this will have any 2 random values

#iterators

integers = [0, 1, 2, 3]
i_integers = iter(integers)
print(type(i_integers))

scores = {'John': 99, 'Danny': 95}
i_scores = iter(scores)
print(type(i_scores))

#<class 'list_iterator'>
#<class 'dict_keyiterator'>

# you can choose where to yield From

def custom_chain(*iterables):
    for iterable in iterables:
        yield from iterable

for x in custom_chain([1, 2, 3], 'abc'):
    print(x, end=' ')

# send information back to the Generator


def pool_money(bet, amount):
    while True:
        amount += bet
        bet = yield amount

pool_money_gen = pool_money(0, 100)
print(f'* The beginning: {next(pool_money_gen)}')
# Get the bet from the user, let's assume they're 20 and 50 for two rounds
print(f'* After the second bet of 20: {pool_money_gen.send(20)}')
print(f'* After the third bet of 50: {pool_money_gen.send(50)}')


#1. Get the absolute path of the file where the code is located:
current_path = os.path.abspath(__file__)

#2. Get the directory where the above files are located
current_dir = os.path.dirname(os.path.abspath(__file__))

#3.This is the upper-level directory to get the current file
os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#4.This is set the environment variable to add the path to the system
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


"""
1. Merge two dictionaries in a single expression
If you use Python3.9 and above, you can use | for this purpose.
"""
x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}
z = x | y

# If you want to assign the result to the first dictionary, you can simply use |=

# 2. Merge two lists
x = ['a', 'b']
y = ['c', 'd', 'e']
x.extend(y)
print(x)
#or
x += y

"""
5. Get the longest string from a list
Suppose we have a list consisting of words:
and we want to get the longest word in this list. All we need to do is that:
"""
words = ['Python', 'is', 'awesome']
max(words, key=len)

"""
9. Read a file in a single line
And now let’s try to read what we’ve just written to the file.
Compared to other programming languages such as Java or C++ , reading a file in Python is pretty easy.
"""
data = [line.strip() for line in open("file.txt")]

fib = lambda x: x if x <= 1 else fib(x - 1) + fib(x - 2)

'I love Python'.count('o')

# 14. Sort in a single line
numbers = [5, -3, 428, -102, 4, 1]
numbers.sort()
print(numbers)

# What if we want to sort it in the reverse order? Then pass reverse=True as an argument.
numbers.sort(reverse=True)
print(numbers)

# 15. Create a dictionary from a list
cars = ['Audi', 'BMW', 'Ford', 'Volkswagen', 'Volvo']
cars_dict = dict(enumerate(cars))

# 16. Create a dictionary with key-value pair
dict(name='Jack', country= 'USA', age=25)

# 22. Convert a list of strings to integers
# We will use map() function here. Remember that map() takes two arguments: a function and an iterable. It applies the function to each item of the iterable.
list(map(int, ['1', '2', '3']))

print(*range(1, 6), sep='\n')


from pathlib import Path
filepath = Path('/Users/jlee/test_dir/test1.txt')

Path.home()
#PosixPath('/Users/jlee')
Path.cwd()
#PosixPath('/Users/jlee/test_dir')

filepath.parent
#PosixPath('/Users/jlee/test_dir')

# This replaces the following more verbose os.path.dirname function:
import os

os.path.dirname(os.path.abspath('test1.txt'))
#'/Users/jlee/test_dir'

# Confirm the type of path with:
filepath.is_dir()
# False
filepath.is_file()
# True

# 1. Get string representations of path objects and their components

filepath.as_posix()
# '/Users/jlee/test_dir/test1.txt'
str(filepath)
# '/Users/jlee/test_dir/test1.txt'
filepath.name
# 'test1.txt'
filepath.stem
# 'test1'
filepath.suffix
# '.txt'

# 2. Create child paths using the slash operator
# One of my favorite aspects of pathlib is that it provides a much more intuitive and cleaner way to build up paths. Simply insert the slash operator (/) between a Path object and a path string to create a new path object:
filepath = Path.cwd() / "test1.txt"
# PosixPath('/Users/jlee/test_dir/test1.txt')
filepath2 = Path.cwd() / "test3.txt"
# PosixPath('/Users/jlee/test_dir/test3.txt')
filepath3 = Path.cwd() / "embedded_dir/test3.txt"
# PosixPath('/Users/jlee/test_dir/embedded_dir/test3.txt')
# Check whether these paths exist using .exists().
filepath.exists()
# True
filepath2.exists()
# False
filepath3.exists()
# True

# 3. List all files in a directory matching a pattern
dirpath = filepath.parent
# >>> [f for f in dirpath.iterdir() if f.is_file()]
# [PosixPath('/Users/jlee/test_dir/test1.txt'), PosixPath('/Users/jlee/test_dir/test2.txt')]
# Use .glob(pattern) to find all files in a specified directory matching a pattern, e.g., all .txt files:
dirpath = Path.cwd()
files = dirpath.glob("*.txt")
list(files)
# [PosixPath('/Users/jlee/test_dir/test1.txt'), PosixPath('/Users/jlee/test_dir/test2.txt')]
# Add "**/" to the beginning of the pattern to traverse the current directory and all subdirectories:
all_files = dirpath.glob("**/*.txt")
list(all_files)
# [PosixPath('/Users/jlee/test_dir/test1.txt'), PosixPath('/Users/jlee/test_dir/test2.txt'), PosixPath('/Users/jlee/test_dir/embedded_dir/test3.txt')]
# Alternatively, use .rglob (for “recursive glob”) if you don’t want to use "**/":
list(dirpath.rglob("*.txt"))
# [PosixPath('/Users/jlee/test_dir/test1.txt'), PosixPath('/Users/jlee/test_dir/test2.txt'), PosixPath('/Users/jlee/test_dir/embedded_dir/test3.txt')]
# This replaces the much more lengthy: 😐
import os
paths = []
for root, subdir, files in os.walk(dirpath):
    for f in files:
        if f.endswith(".txt"):
            paths.append(str(os.path.join(root, f)))

# 4. Get the full path of a file or directory
# The .resolve() method will return a new path object with the absolute path while resolving any symlinks and eliminating any .. components.
Path('embedded_dir').resolve()
# PosixPath('/Users/jlee/test_dir/embedded_dir')
# cf
Path('embedded_dir')
# PosixPath('embedded_dir')

# 5. For use in a running script
# If you’re working with a Python module, you will need to use the variable __file__ to get the path of the running script file. When the module is loaded, __file__ is set to the path of the .py file. Using __file__ with other functions allows you to refer to directories relative to this path.
# The old way to accomplish this was:
# inside, say, utils/__init__.py
import os
SOURCE_FILE = os.path.abspath(__file__)
SOURCE_DIR = os.path.dirname(SOURCE_FILE)  # /Users/jlee/test_dir
ROOT_DIR = os.path.abspath(os.path.join(SOURCE_DIR , ".."))  # /Users/jlee
EMBEDDED_DIR = os.path.join(os.path.dirname(__file__), os.path.abspath("embedded_dir"))  # /Users/jlee/test_dir/embedded_dir

# Using Path, you can express this in a much more concise way:
from pathlib import Path
SOURCE_FILE = Path(__file__).resolve()
SOURCE_DIR = SOURCE_FILE.parent
ROOT_DIR = SOURCE_DIR.parent
EMBEDDED_DIR = SOURCE_DIR / "embedded_dir"