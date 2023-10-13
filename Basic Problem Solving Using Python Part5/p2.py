

# python prog to print sum of number  digits in a list 

# creating a list 

l1=[12,23,34,45,56]

print("The original list is", l1)

rest=[] # creating an empty list to store values 

total=0

# using  a for loop

for elements in l1:

       for i in str(elements):

              total+=int(i)

       rest.append(total)

print(f"The sum of digits in a list {l1} is ", str(rest))