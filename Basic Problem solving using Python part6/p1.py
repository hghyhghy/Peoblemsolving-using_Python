

# python program to accept the strings which are  vowels 


# creating a function first

def ofcheck(s):

       s=s.lower() # making all to lower case characters 

       # setting the vowels 

       vowels = set("aeiou")

       # creating an empty dict

       s=set({})

       # iterating through the loop

       for chars in s:

              if chars in vowels:

                     s.add(chars)

              else:
                     pass

       if len(s)==len(vowels):

              print("Accepted")

       else:
              print("Not Accepted ")

s="aeiou"

ofcheck(s)