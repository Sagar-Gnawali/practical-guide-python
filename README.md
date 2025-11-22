# Notes

- These are Python notes with a few code examples for anyone who wants to get started with Python programming.

# Python

- Python is the dynamic language
- In python the naming convention is varibale is must be lower case and separated with underscore

# Python Setup

- python3 -m venv env
- source env/bin/activate (to activate env or virtual environment)
- https://peps.python.org/pep-0008/ for python standards
- https://pypi.org/ for pyhton packages like npmjs.com for npm libraries
  This contain standalone python version or standalone python interpretor.
- import antigravity

# After running the virtual env

- We can run python code in termial using `python file_name.py`
- Or we can use `cmd+shift+p` and run python file in Terminal

# REPL

- REPL Stands for Read, Evaluate, Print and Loop. It allows you to interactively type in Python program line-by-line.
- Note , in the REPL three arrows `>>>` indicate a line of input given at the prompt
- In the REPL # will be ignored
- `control+D` to exist just simply type/execute `exit()` while you're in REPL
- Helpful REPL method: `help()`, `type()` and `dir()`

# help()

- if we want to need docs for something we can use it
- en: help(str), help('some_topic')
- eg: help(str.isalpha)

# type()

- Used to find the type of the data
- eg: a = 10 ; type(a)

# dir()

- It will going to show the directory of all the methods that are availabe for that type
- If I want to know the all the methods of the string we can use `dir(str)`

# Code running

- if `__name__` = `"__main__"` when we are using python program from command line this is the entry point

# Special name

- print(f"{data}")
- print(r"") for regular expression
- print(b"") for byte String

# Variables and Data types

- variable name must me small case or separated by underscore
- variable can not be start with special symbol or number
- In python everything is an object
- Don't name your variable thiings like int, str, list etc.
- Differnce in Null and None
- If we want to initialize and declare with nothing or no value we can use None eg: `data=None`

# Data types

- Text type: `str`
- Numeric type: `int`, `float`, `complex`
- Sequence types: `list`, `tuple`,`range`
- Mapping type: `dict`
- Set types: `set` , `frozenset`
- Boolean type: `bool`
- Binary Types: `bytes`, `bytearray`, `memoryview`
- NoneType: `NoneType` None

## Integer

- a =10
- b =-190

## float

- b=90.2
- c= 0. (this is also valid float)
- type(c)

## Complex number

- The number which end with j
- a = 78j
- type(a)

The types are object under the hood we can also declare them by calling the constructor for that built in type

- a = int(5)
- b = float(9)
- c = complex(89)

# Math or number methods

- min(12,3,4)
- max(4,5,4)
- round(23.51) -> 24

# Boolean

- In python the boolean are represent using `True` and `False` with first upper case letter

# String

- data = "python" or data = 'python'
- Python accept both single and double quote
- Always use double quote for string
- In the REPL if we want to add long string we can use """ start and """ end

- a = "zoozle'
- a.repalce('z','g') -> google
- this will not modified the original a , in order to do so we need to assign it a
- a = a.replace('z','g')

# list

- List are used to store multiple items in a single variable
- We can change specific index value in lists
- programming = ["Python", "Java", "Javascript"]
- programming[0]="ruby"

# Tuples

- Tuples are light-weight collections used to keep track of related, but different items.
- Tuples are immutiable ie once a tuple has been created the item in it cann't be change. We cann't add, update and remove items.

# Sets

- Set is a mutable data type that allows you to store immutable types in an unsorted way.
- Sets are mutable because you can add and remove items from them. They can contain immutable items, like `tuple`s and other primitive types, but not `lists`s , `set`s and `dict`ionaries which are themselves mutable.
- A set is a collection which is unordered, unchangeable, and unindexed.
- Unordered means that items in a set do not have a defined order.
- Sets have fast memebership testing
- Set can not contain dublicate value
- data ={3,3,3,2}
- print(data) -> {3,2}

# Dictionaries

- Dictionaris are a useful type that allow us to store our data in key, value pairs. Dictionaries themselves are mutable, but just like sets dictionary keys can only be immutable types.
- Dictonary don't have order like set.
- Create dic: my_dict={"name":"name","email":"gnawali@gmail.com"}
- To access value we need to pass key eg: my_dict['name']
- If we tried to access value with key which doesn't exists and we did not want error message we can use `my_dict.get('key_name')`
- The `get()` method have the second argument like `my_dict.get('key_name', 'default_value')` which give the default_value of key_name if the key_name is not exists in the dictionary

- To get all the keys we can use .keys() `my_dict.keys()`
- To get all the values we can use .values() eg: `my_dict.values()`
- while working with dict most of the time will use .items() eg: `my_dict.items()`

# Functions

- Funciton can be defined in python using `def fxn_name`
- Don't use mutable types as default arguments

# Check true and false

- list1 = [1,2,3]
- list2 = [1,2,3]
- list1 === list2 True
- list1 is list2 -> False # checks for identity. Do they point to the same place in memeory?
- Don't use if something is true or not by using `a==True` instead use `a is True`
- Python has `and` , `or` and `not` for checking

# Enumerate

- To get index and data
- colors =['red','green','pink']
  eg:

  ```python
  for index,color in enumerate(colors):
        print(f"index: {index} color: {color}")
  ```

# Comprehension

- list comprehension
- dictionary comprehension

# Generator

-

# OOPS

- Object-Oriented Prgramming (OOP) is a language model (or paradigm) in which properties or behaviours are organized into "Object".

# isinstance(object, class_or_tuple)

- It Checks if an object is an instance of a class or a tuple of classes.
- eg: isinstance(10,int) return true because 10 is instance of int

# Magic method

- these are those which are start with `__` and end with `__`
- These are special methods
- eg: `__init__()`
- Some special magic method which are used frequently `__str__` `__init__`
- `__repr__` not used that much

- `__str__` is the representation of your object that should be human readable

# Libraries ,Modules and Imports

- python -m pip install lib_name
- python -m pip install requests

- import from random (it will imports all the module)
- from random import randint (it will import only randint)
