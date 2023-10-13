# printing all positive numbers from the list

# creating a list first

l1 = [21, -3, -4, 12, 5]

# initializing a variable num with 0

num = 0

# running a while loop

while (num < len(l1)):
    
    if l1[num] >= 0:
        
        
        print(f"The positive numbers from the list {l1}  is ",l1[num])

    num += 1  # incrementing the variable in each iteration


# printing all negative numbers from the list by using while loop


l2=[-1,0,-2,100,65]

num1=0

# using a while loop

while(num1<len(l2)):
    
    if l2[num1]<0:
        
       print(f"The numbers from the list {l2}  is ", l2[num1])
       
    num1+=1

       




