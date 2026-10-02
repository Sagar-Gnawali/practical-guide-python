'''
e) Write a Python program to add ‘ing’ at the end of a given string (length should be at least 3). If
the given string already ends with ‘ing’ then add ‘ly’ instead. If the string length of the given string
is less than 3, leave it unchanged. Sample string: ‘abc’ Expected result : ‘abcing’ Sample string :
‘string’ Expected Result : ‘stringly’ Tip: you might want to check the string methods .endswith() or
.startswith().
'''
def addIng(val):
    return f"{val}ing"

def addLy(val):
    return f"{val}ly"

def stringManipulation(str):
    if len(str) >= 3:
        if str.endswith("ing"):
            return addLy(str)
        elif str.endswith("ly"):
            return addIng(str)
        else:
            return addIng(str)
    return str

print(stringManipulation("ab"))
