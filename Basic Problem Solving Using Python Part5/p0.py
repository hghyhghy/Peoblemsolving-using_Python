# removing empty tuples from the list

# ceating a function


def toRemove(tuples):
    # using a for loop

    for i in tuples:
        # using a if loop

        if len(i) == 0:
            
            tuples.remove(i)

        return tuples


tuples = [(), (1, 2, 3), (""), (4, 5)]


print(
    f"After removing the empty tuples form the list {tuples}  it becomes",
    toRemove(tuples),
)

# approach 2 by using inbuilt python method filter

# creating a function 

def ofremove(l1):
    
    l1=filter(None,l1)

    return l1

l1=[(),(1,2,3),("",""),("Subham and Shreyoshi")]

print(f"After removing empty tuples from the list {l1}  it becomes   ",ofremove(l1))

# approach 3

def remove(l2):
    
    for i in l2:
        
       if i==():
            
            l2.remove(i)

       return l2
    
l2=[(),(1,2,3),("",""),("Subham and Shreyoshi")]

print(f"After removing empty tuples from the list {l2}  it becomes   ",remove(l2))




