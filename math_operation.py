import math
a = 20.23
print(round(a))  # it will round the value of a to nearest integer

print(round(a, 1))  # it will round the value of a to 1 decimal place

print(abs(-29))

print(min(201, 12, 20, 3))

print(max(20, 23, 563, 356, 875))

print(math.ceil(a))  # 21

print(math.floor(a))  # 20

print(int(math.sqrt(16)))

print(math.factorial(5))

print(math.pi)  # 3.141592653589793

b = math.nan
print(type(b))  # <class 'float'>

print(type(float('nan')))  # <class 'float'>
# to check for nan
# nan is not equal to anything, including itself
if math.isnan(b):
    print("b is nan")
else:
    print("b is not nan")
