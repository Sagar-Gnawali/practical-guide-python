colors = ['red', "green", "blue","Black"]

for color in colors:
    print(color)

print("outside color:", color) # we can access the loop variable outside the loop because it is defined in the same scope and it will going to print the last value of the loop variable

#To get index and value we can use enumerate() function
for index, color in enumerate(colors):
    print(f"index: {index} color: {color}")

# Iterate dictonary
hex_colors = {'red': '#FF0000', 'green': '#00FF00', 'blue': '#0000FF'}
for color, hex in hex_colors.items():
    print(f"color: {color} hex: {hex}")