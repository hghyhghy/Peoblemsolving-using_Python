

# python program to print even length words from a string 

# creating a string first

s="Hey python I want to learn You "

# splitting the string 

s1=s.split()

# using the for loop

for x in s1:

       if len(x)%2==0:

              print(x)

# approach 2 by using a function 

def ofcount(s):

       s=s.split()

       # using a for loop 

       for i in s:

              if len(i)%2==0:

                     return i

s="Me and Mom and Dad"

print(f"The even length words from the string {s}  is ", ofcount(s))
              










