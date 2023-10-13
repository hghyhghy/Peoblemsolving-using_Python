

# python program to find cumulative sum of a list 

# creating list of integers

l1=[10,20,30,40,50,60]

# calculating the length of the list 

length=len(l1)

print(length)

temp=[] # creating an empty list to store summed values 

j=0 # creating a variable and initializes with 0

# using a for loop

for x in range(0,length):

       j=j+l1[x]

       temp.append(j)

print(f"The cumulative  sum of the list {l1}  is " , temp)

       