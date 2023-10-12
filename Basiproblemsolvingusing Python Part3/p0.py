# python program to print even numbers from a list

list = [2, 4, 8, 9, 7, 5]

# creatin a for loop to print the even numbers

for num in list:
    
    if num % 2 == 0:
        
        print(num, end=" ")


#  approach 2 by using while loop

list1 = [23, 44, 56, 2, 4, 99]

# creating a variable num and initializes by 0

num1 = 0

# running a while loop

while num1 < len(list1):
    
    if list1[num1] % 2 == 0:
        
        print(f"The even numbers from the list {list1}  is ", list1[num1])

    num1 += 1
