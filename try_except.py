# The try except Block in Python
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The finally block lets you execute the code regardless of the result of try-except

try: 
    print(data)
except Exception as e:
    print("some error occured", e)
finally:
    print("This will execute no matter what!")