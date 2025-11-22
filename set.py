# Create set 
data ={1,2,3,4,2}
print(data) # {1, 2, 3, 4} duplicate value will be removed

# if we have lists with duplicate value and we want to remove duplicate value we can convert list to set
numbers = [1,2,4,5,5,6,7,8,8,9]
unique_numbers = set(numbers)
print(unique_numbers) 
print(list(unique_numbers)) # convert set to list

# Shortcut to check mutability
# hash()
print(hash(10))
# print(hash([]))
print(hash(()))

# Sets don't have an order 
# Means if we put a buch of items in the set it will not going to maintain the order
my_set ={"data",4,523,"Hello"}
print(my_set) # it will print in random order 

# We can not access item by index because set don't have an order
# print(my_set[0]) # TypeError: 'set' object is not subscriptable

# to add item to sets
my_set.add("new item")
print(my_set)

# To remove item from the set
my_set.discard("data") 
print(my_set)

# Contact two sets
set1={1,2,3}
set2={4,6,5}
set1.update(set2) # it will add all the items from set2 to set1
print(set1)