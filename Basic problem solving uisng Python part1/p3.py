

# checking wheather a string is palindrome or not 

# creating a string 

mystring="saBbas"

mystring=mystring.casefold() # returns the version of the string suitable for caseless comparison

# reversing a string 

revstr=reversed(mystring)

if list(mystring)==list(revstr):

       print(f"The string {mystring} is palindrome ")

else:
       print(f"The string {mystring} is not palindrome ")