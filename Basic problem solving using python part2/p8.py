

# printing the second largest number in the list 

# creating a list first 

list=[23,45,12,56,8]

# sorting the element in the list 

list.sort()

print(f"The smallest number form the list {list}  is ", list[0])

print(f"The largest number form the list {list}  is ", list[-1])

print(f"The second largest  number form the list {list}  is ", list[-2])

# approach 2 removing the largest number form the list

l1=[2,3,4,5,1,7,99]

newl=set(l1)

# removing the largest element 

newl.remove(max(l1))

print("The largest element form the list is ", max(newl))
