# python program to interchange the first and last  elements in a list

# approach 1

# creating a function


def ofswap(list):
    size = len(list)

    # creating a variable and store it in that

    temp = list[0]

    list[0] = list[size - 1]

    list[size - 1] = temp

    return list


list = [12, 34, 5, 6, 89]

print(f"The interchanged version of the list {list}  is ", ofswap(list))


# approach 2


def ofswap1(list1):
    list1[0], list1[-1] = list1[-1], list1[0]

    return list1


list1 = [2, 3, 4, 5, 6]

print(f"The swapped version of the list {list1}  is ", ofswap1(list1))

# interchanging the 1th element with other element


def ofswap3(num):
    l = len(num)

    temp1 = num[1]

    num[1] = num[l - 2]

    num[l - 2] = temp1

    return num


num = [2, 3, 4, 5, 6, 7]

print(f"The swapped version of the list {num} is  ", ofswap3(num))
