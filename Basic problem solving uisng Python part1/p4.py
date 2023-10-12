# python program to remove all the punctuations from a string


punc = "'''[]!{}();:,\,<>,-,?,/,@,#.$,%,^,*,_,="

# printing a string

mystr = "Hello!!! Lets go ==== for a dinner ?"

# to remove all punctuations from the string lets firts create a empty string

newstr = ""

for chars in mystr:
    if chars not in punc:
        newstr = newstr + chars

print(newstr)
