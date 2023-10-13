
from collections import Counter

# python program to find words frequency in a given string 

# creating a string first

s="Hey there look like a guitarist like me there  "

# spliting the words  in the string 

temp=s.split()

# counting the words frequency

re=Counter(temp)

print("The words frequency are ", str(dict(re)))