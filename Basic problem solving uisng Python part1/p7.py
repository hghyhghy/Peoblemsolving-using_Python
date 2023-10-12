# python program to find the sum of the array

# creating a function


def ofsum(arr):
    sum = 0

    for i in arr:
        sum = sum + i

        print(sum)


arr = [1, 2, 3, 4, 5]

print(ofsum(arr))


# by using the sum()  method

arr = [1, 2, 3, 4, 5, 6]

answer = sum(arr)

print(answer)
