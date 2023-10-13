

# printing all odd numbers from a given range by using python 

start =8

end= 20

# usimg a for loop

for i in range(start,end+1):

       if i%2!=0:

              print(f"The odd number from that range {start} to {end}  is  ", i)


# approach 2 by only using if else loop

a=4 

b=20

# use a for loop

for i in range(a,b+1):

       if i%2==0:

              pass
       else:
              print(f"The odd numbers from the  range {a}  to {b}  is ",i)