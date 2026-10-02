'''
Write a Python program that adds <div> HTML tags around a string. For example, a string
“Python is cool” should be surrounded with <div> tags and the result is: “<div>Python is
cool</div>”
'''
def addHtmlTag(val):
    withDivTag = ""
    if type(val) == str and len(val) > 0:
        withDivTag = f"<div>{val}</div>"

    return withDivTag

print(addHtmlTag("my files"))
print(addHtmlTag(""))

