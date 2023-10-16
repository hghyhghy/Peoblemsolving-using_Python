

# python program to remove the ith character from the string 

# creating a function 

def ofremove(s1,i): # taking two arguments 

       n=s1[0:i] # storing the letters from 0 to i

       n1=s1[i+1:len(s1)] # storing the elements  after i to the rest 

       return n+n1

s1="Subham  love Shreyoshi "

i=6

print(ofremove(s1,i))

# approach 2 

# creating a function 

def remove(s2,k):

       for i in range (len(s2)):

              if i==k:

                     s2=s2.replace(s2[k]," ",1)

       return s2


s2="Subham and Shreyoshi"

i=6

print(remove(s2,i))

