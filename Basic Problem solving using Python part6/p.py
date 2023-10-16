

# to find the length of the string in python 

# first approach 

# creating a string first 

string="Subham and Shreyoshi"

print(f"The length of the string {string}  is ", len(string))

# now by using for loop

#second approach 

def oflength(s1):

       counter=0

       # using a for  loop

       for y in s1:

              counter+=1

       return counter

s1="We and us"

print(f"The length of the string {s1}  is ", oflength(s1))

# approach 3 

# by using while loop

def le(s2):

       counter1=0 # initializing the variable with zero

       while s2[counter1:len(s1)]:

              counter1+=1

       return counter1

s2="Shreyoshi"

print(f"The length of the string {s2}  is ", le(s2))

