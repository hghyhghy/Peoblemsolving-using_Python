# python program to check wheather a string is binary string or not

# creating a function


def ofcheck(string):
    # set function use to  set a string into a set of characters

    s1 = set(string)

    s = {"0", "1"}

    # for checking we use if else loop

    if s == s1 or s1 == "0" or s1 == "1":
        print(f"The string {string}  is a binary string")

    else:
        print(f"The string {string}  is not a binary string")


string = "01001001"

ofcheck(string)

# approach 2

#  by using string count function

string1 = "010011001011"

if string1.count("0") + string1.count("1") == len(string1):
    print("Yes ")

else:
    print("No")
