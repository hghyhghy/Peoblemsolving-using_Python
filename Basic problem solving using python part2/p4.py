# python program to find the sum of all elements in a list

# creating a list

list = [12, 13, 14, 15, 16]

# initializing a vaiable of total

total = 0

# interating through the loop by using for loop


for ele in range(0, len(list)):
    total = total + list[ele]

print(f"The sum of the elements present in the list {list}  is ", total)

# approach 3 by using while loop

total = 0

ele = 0

l1 = [1, 2, 3, 4, 5]

# running a while loop

while ele < len(l1):
    total = total + l1[ele]

    ele += 1

print(f"The sum of the elements present in the list {l1}  is ", total)

# approach 4 by using sum()  method 

lis=[2,3,4,5,6,7,8,9]

# initializing a variable to store the sum value 

temp=sum(lis)

print(f"The sum of the elements present in the list {lis}  is " ,temp)
