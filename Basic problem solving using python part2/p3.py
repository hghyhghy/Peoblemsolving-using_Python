# reversing a list by using slicing method


# creating a function


def ofreverse(list):
    
    newlist = list[::-1]

    return newlist


list = [0, 1, 2, 3, 4]

print(f"The reversed version of the list {list}  is ", ofreverse(list))

# approach 2


# to reverse a list by using python in built function

l1 = [1, 2, 3, 4, 5, 6, 7]

l1.reverse()

print(f"The reversed version of the list is ", l1)

# approach 3

# reversing the list by using insert()  function 

lst=[10,11,12,13,14,15]

# creating an empty list 

l1=[]

# running a for loop

for i in lst:
    
    l1.insert(0,i)

print(f"The reversed version of the list {lst} is ", l1)
