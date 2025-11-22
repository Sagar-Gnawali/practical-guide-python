# get the length of the name in list
my_name =["Dominic","Taylor","Tommy","John"]
len_name = [len(name) for name in my_name]
print(len_name) # [7, 6, 5, 4]

# Traditional way 
len_name2 = []
for i in my_name:
    len_name2.append(len(i))

print(len_name2) # [7, 6, 5, 4]