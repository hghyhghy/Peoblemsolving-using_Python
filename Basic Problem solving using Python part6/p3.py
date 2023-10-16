# find words whicg are greater than of a given length of k in python

# craeting a function first


def ofcreate(s1, num):  # function taking two arguments
    # creating an empty string

    s2 = []

    # splitting the string

    temp = s1.split()

    # using a for loop

    for x in temp:
        if len(x) > num:
            s2.append(x)
    return s2


s1 = "Subham and shreyoshi do love each other"

num = 4

print(ofcreate(s1, num))

# method 2 using list comprehension

sen = "Hey Python Looks like you are so interesting , Allow me to learn you "

length = 4  # defining the length


print([word for word in sen.split() if len(sen)>length])