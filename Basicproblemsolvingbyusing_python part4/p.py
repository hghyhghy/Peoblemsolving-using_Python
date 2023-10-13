# print of all even numbers from a fiven range

# by using a for loop

for evennumbers in range(4, 15, 2):  # two 2 is gap between two numbers
    
    print(evennumbers, end=" ")


# approach 2 by taking user inputs

start = int(input("Enter the starting number ::"))

end = int(input("Enter the ending  number ::"))

# by using a for loop

for num in range(start, end+1):
    
    if num % 2 == 0:
        
        print("The even numbers from the range are ", num, end=" ")

# approach 3 

# by only using if else loop

a=4

b=16

# for loop

for i in range(a,b+1):
    
    if i%2!=0:
        
        pass
    else:
        
        print(i)


