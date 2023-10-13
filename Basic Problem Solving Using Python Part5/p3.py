

# break a list into chunks of size N in python 

# creating a list

l1=[1,2,3,4,5,6,7,8,9]

start=0

end=len(l1)

gap=3 # gap b2win two lists

# using a for loop

for i in range(start,end,gap):

       

       print(l1[i:i+gap])
