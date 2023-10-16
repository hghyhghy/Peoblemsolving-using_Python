from itertools import permutations

# permutation of a given string by using pythons inbuilt function

# creating a function


def ofpermutation(st):
    permu = permutations(st)

    # printing all permutations

    for perm in permu:
        print("".join(perm))


st = "123"

(ofpermutation(st))

# approach 2

# by using if else loop

s = "ABC"

p = permutations(s)

# creating an empty dictionary

d = []

for i in list(p):
    if i not in d:
        d.append(i)

        print("".join(i))


# EVALUATE A STRING OF CODE BY USING EVAL()  FUNCTION

soup = "110+120"

result = eval(soup)

print(result)
