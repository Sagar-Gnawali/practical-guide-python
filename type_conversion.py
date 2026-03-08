# Some of the python built-in functions are used to convert one data to another
# int() - converts a value to an integer
# float() - converts a value to a floating-point number
# str() - converts a value to a string
# bool() - converts a value to a boolean
# list() - converts a value to a list
# tuple() - converts a value to a tuple
# set() - converts a value to a set
# dict() - converts a value to a dictionary
print(bool('s'))  # True
print(bool(' '))  # True because it is not empty string
print(bool(''))  # False because it is empty string

print(bool(0))  # False
print(bool(1))  # True
print(bool(-1))  # True because it is not zero
print(bool([]))  # False because it is empty list

print(str(23.23))  # '23.23'

print(int(2232.23))  # 2232

print(float(392))  # 392.0
print(float('23.23'))  # 23.23

print(complex(4, 3))  # (4+3j)


print(list('python'))  # ['p', 'y', 't', 'h', 'o', 'n']
print(tuple('python'))  # ('p', 'y', 't', 'h', 'o', 'n') un-order
print(set('pythono'))  # {'y', 'h', 'n', 't', 'o', 'p'} un-order and unique
print(dict(a=12, b=12, x=10))  # {'a': 12, 'b': 12, 'x': 10}

# conversion from tuple to list
print(list((2, 3, 41, 1)))

# conversion from list to tuple
print(tuple([2, 3, 41, 1]))

# conversion from list to set
# {41, 2, 3, 1} 1 and 2 are repeated but set will only keep unique values
print(set([2, 3, 41, 1, 2, 1]))

# conversion from set to list
print(list({3, 4, 2, 2}))  # [2, 3, 4]

# conversion from set to tuple
print(tuple({2, 3, 41, 1}))


print(bool(float('nan')))  # True because it is not zero
