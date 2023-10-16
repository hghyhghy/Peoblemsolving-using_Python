

# python program to join and split a string 

# creating a function 

def ofsplit(s1):

       list1=s1.split(" ")

       return list1

def ofjoin(s1):

       s2="-".join(s1)

       return s2

s1="Subham and shreyoshi"

list1=ofsplit(s1)

print(list1)

s2=ofjoin(s1)

print(s2)

# by using inbuilt function 

s="Subham and Shreyoshi"

print(s.split(" "))

print("-".join(s))