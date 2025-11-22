"""
We can not access the local variable outside the function it will give error
We can access the global variable inside the function
"""
a = 10 # global variable
def fun():
    x = 20 #local variable
    print("inside function",x) 

fun()
# print("outside function",x) we can not access local variable outside the function it will give NameError
print("outside function",a)

"""
To change the value of the global variable inside the function we need to use `global` keyword
"""

user_name="garry"
def change_name():
    global user_name
    user_name="sagar"
    print("inside function",user_name)


change_name()
print("outside function",user_name)