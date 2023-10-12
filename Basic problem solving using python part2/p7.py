# python program to print  the largest element ina list

list1 = [2, 3, 4, 1, 5, 99, 0, 7]

# sorting the  elements in the list

list1.sort()

print(f"The largest value in the list {list1}  is  ", list1[-1])


# approach 2 by using max()

l1 = [2, 3, 1, 4, 0, 8]

print(f"The largest element in th list {l1}  is ", max(l1))

# without using built in functions 

# creating a function 

def oflargest(list):

       # assuming that first number is largest and assined it to a variable maximum

       maximum=list[0]

       # uysing a for loop

       for x in list:

              if x>maximum:

                     maximum=x
       return x

list=[23,12,34,13,9999]

print(f"The largest element from the list {list}  is ", oflargest(list))




