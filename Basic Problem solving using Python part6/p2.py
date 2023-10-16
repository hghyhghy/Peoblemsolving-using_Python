# python program to check wheather a special character is present in a string or not

import string

# creating a string

# s1 = "Subham@#%"

# # creating a variable to store the values

# c = 0

# s2 = "[!,@,#,$,%,^,&,*,<>,?,:]"  # the special characters

# # spliting the string

# s1.split()


# # using a  for loop

# for i in range(len(s1)):
    
#     if s1[i] in s2:
        
#         c += 1
# if c:
#     print("String is not accepted ")

# else:
#     print("Accepted")


# by using string.punctuation 

# creating a function 

def ofcheck(s1):
    
    # using a for loop

    for i in s1 :
        
        if i in  string.punctuation:
            
            print(f"The {s1} is not accepted ")

            return
        
    print(f"String {s1} is not accepted ")

        


ofcheck("Subham & Shreyoshi")

