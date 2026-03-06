# String in python are immutable
data = "programming"

# data[0] = "P"  # This will give error because string are immutable
print(data.count('r'))  # 2
print(data.upper())  # PROGRAMMING
print(data.lower())  # programming
print(data.replace('g', 'G'))  # proGramminG
print(data.find('m'))  # 6 (index of first occurrence)
print(data.find('z'))  # -1 (not found)
print(data.split('m'))  # ['progra', 'min', 'g']
print(data.startswith('pro'))  # True
print(data.endswith('ing'))  # True
print(data.isalpha())  # True (only letters)
print(data.isdigit())  # False (not only digits)
print(data.isalnum())  # True (only letters and digits)
print(len(data))  # 11
print(" Test data. ".strip())  # to remove leading and trailing whitespace
print(data)
