
import copy

# copying or cloning a list  in python 

# creating a function for that 

def ofcopy(l1):

       newl=[] # creating an empty list 

       newl.extend(l1) # extending the val of l1

       return newl

l1=[2,3,4,5,6]

l2=ofcopy(l1)

print("Original list", l1)

print("Copied list", l2)

# approach 2 

# by using deepcopy

li=[1,2,4,6,8]

l=copy.deepcopy(li)

print(f"The copied version of {li}  is ", l)

