# printing all duplicate items from a string by using python

# creating a function


def ofsearch(st):
    # creating an empty dictionary

    x = []

    # using a for loop

    for i in st:
        if i not in x and st.count(i) > 1:
            x.append(i)

    print("".join(x))


st = "Subham and Shreyoshi"

ofsearch(st)


# python program to replace all occurances of a substring in a string

# creating a string first

s1 = "England Will Win The Cricket WorldCup"

s2 = "England"

S3 = "India"

print(f"The replaced Version of the string {s1} is ", s1.replace(s2, S3))
