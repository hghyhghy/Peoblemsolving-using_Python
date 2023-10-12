
import math

# importing numpy 



# multiply all  numbers in a list 

# cresating  a function  first to multiply



def ofmultiply(mylist):

       result=1 # creating a variable to use 

       for i in mylist:

              result=result*i

       return result
 
l1=[2,3,4]


print(f"The multiplied value of the list {l1}  is ", ofmultiply(l1))


# approach 2 by using  math module 


l2=[1,2,3]

result1=math.prod(l2)

print(f"The multiplied value of the list {l2}  is ", result1)




