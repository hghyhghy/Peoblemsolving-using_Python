# python program to print uncommon words from two strings


# creating a function


def ofcheck(a, b):
    a = a.split()

    # spliting  the strings

    b = b.split()

    # creating an empty list

    x = []

    for i in a:
        if i not in b:
            x.append(i)

    # using another for  loop

    for i in b:
        if i not in a:
            x.append(i)

    x = list(set(x))

    return x


a = "Subham and Shreyoshi"

b = "Subham and Shrestha"

print(ofcheck(a, b))
