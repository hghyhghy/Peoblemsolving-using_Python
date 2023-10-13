



# python program to reverse the words in the string 

# creating a string 

string="name my is Subham"

s=string.split()[::-1]

# creating an empty list to store values 

l=[]

for i in s:

       l.append(i)


print(" ".join(l))

