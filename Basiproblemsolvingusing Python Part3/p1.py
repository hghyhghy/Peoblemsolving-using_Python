# python program to print odd numbers form a list

# creating a list first

# l1=[12,3,4,5,7,8,90,111]

# # using a for loop

# for num in l1:

#        if num%2!=0:

#               print(f"The odd number form the list {l1}  is ", num)


# approach 2 by using while loop

l1 = [12, 1, 32, 34, 33, 19]

num1 = 0

# using a while loop

while num1 < len(l1):
    
    if l1[num1] % 2 != 0:
        
        print(f"The odd numbers from the list {l1}  is ", l1[num1])

    num1 += 1
