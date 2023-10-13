# removing all even numbers from a  list

l1 = [2, 4, 6, 7, 9, 1]

# using a for loop

for x in l1:
    
    if x % 2 == 0:
        
        l1.remove(x)

print("After removing all even numbers from the list it becomes ", l1)


# approach 2 by using del keyword 

l2=[2,3,4,5,6,7,8]

del l2[1:6]

print(l2)