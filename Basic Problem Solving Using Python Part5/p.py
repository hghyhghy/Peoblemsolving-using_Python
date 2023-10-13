

# python program to print duplicate numbers from a list of integers

# creating a list first 

l1=[1,1,2,3,3,4,5,6,6,7,7,8]

unique=[] # creating an empty list 

duplicate=[]

# using a for loop

for i in l1:

       if i not in unique:
              

              unique.append(i)

       elif i not in duplicate:

              duplicate.append(i)

print(duplicate)