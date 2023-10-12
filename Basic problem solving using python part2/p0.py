# swapping two elements in a list by using comma assignment


def ofswap(list, pos1, pos2):
    list[pos1 - 1], list[pos2 - 1] = list[pos2 - 1], list[pos1 - 1]

    return list


list = [23, 65, 19, 90]

pos1 = 1

pos2 = 3

print(ofswap(list, pos1, pos2))

# swapping two numbers by using temporary variable

# creating a function


def swap(list, pos1, pos2):
    # use of the temporary or temp variable

    temp = list[pos1 - 1]

    list[pos1 - 1] = list[pos2 - 1]

    list[pos2 - 1] = temp

    return list


list = [23, 65, 19, 90]

pos1 = 1

pos2 = 3

print(swap(list, pos1, pos2))

# calculating the length of the list by using python inbuilt function

print(len(list))
