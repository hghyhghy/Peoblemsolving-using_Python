

# python program to check wheather a string  is  palindrome or not 

# creating a function

def ispalidrome(s):     # taking an argument s 

       return s==s[::-1]

s="sabbas"

ans=ispalidrome(s)

if ans:

       print(f" {s}  is palindrome ")
else:
       print(f" {s}  is not palindrome ")


# approach 2 by using empty variable 

x="malayalam"

w=""

for i in x:

       w=i+w


if x==w:

       print(f"{x} is palindrome")

else:

       print(f"{x} is not palindrome")



