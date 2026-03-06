# in and not in
# These check whether a value exists inside a container.
# These are also called as membership operators
"""Containers include:
list
tuple
set
string
dictionary
"""

data = "python is programming language"
if 'is' in data:
    print("is is present in data")

if 'java' not in data:
    print("java is not present in data")
else:
    print("java is present in data")

# is and is not
# These check whether two variables refer to the same object in memory, not whether their values are equal.
# These are also called as identity operators
a = [1, 2, 3, 4]
b = a
c = [1, 2, 3, 4]

if a is b:
    print("a and b refer to the same object in memory")
else:
    print("a and b do not refer to the same object in memory")

if a is not c:
    print("a and c do not refer to the same object in memory")
else:
    print("a and c refer to the same object in memory")
