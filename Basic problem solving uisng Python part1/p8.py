# python program to print the largest element in  an array

# creating a function


def oflargest(arr, n):
    # initializing the max value

    max = arr[0]

    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]

    return max


arr = [2, 3, 40, 70]

n = len(arr)

answer = oflargest(arr, n)

print(f"The largest from the array {arr}  is ", answer)

# now by using built in function max()


def oflar(arr1, n):
    arr1 = max(arr1)

    return arr1


arr1 = [30, 50, 10, 1100]

n = len(arr1)

print(f"The largest from the array {arr1}  is ", oflar(arr1, n))
