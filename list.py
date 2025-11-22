# List are used to store multiple items in a single variable.
# Lists are mutable
# Lists are ordered, changeable, and allow duplicate values. 
# lists are defined with square brackets []
# Do not name list as list because it is a built-in function in python

languages = ["Python", "Java", "C++", "JavaScript"]

# can be declared with list() constructor
languages2 = list(("Ruby", "Go", "Swift"))

print(type(languages))  # <class 'list'>

for lan in languages:
    print(lan)

for lan in languages2:
    print(lan)  

# get length of the list
print(len(languages))  

# access item by index
print(languages[0])  

# access last item
print(languages[-1]) 

languages[0]= "Rust" # we can change the value of the list because it is mutable
print(languages) 

lotter_numbers = [8,4,34,6,23]
# Sort lists 
lottery_numbers_sorted= sorted(lotter_numbers) # it will return new sorted list
lottery_sorted_reverse= sorted(lotter_numbers, reverse=True) # it will return new sorted list in reverse order
print(lottery_numbers_sorted)
print(lottery_sorted_reverse)

# If we want to sort the original list we can use sort() method
lotter_numbers.sort()

# Append or add item to the list
lotter_numbers.append(987) 
print(lotter_numbers)

# Add at sepcific index
lotter_numbers.insert(2, 45) 
print((lotter_numbers))

# check if the items exist in the list
if 34 in lotter_numbers:
    print("34 is present in the list")
else:
    print("34 is not present in the list")