# print the factorila of a number  in python

num = int(input("Enter the number "))

factorial = 1

if num < 1:
    print("Could not find the factorial of negative number")

elif num == 0:
    print("The factorial of 0 os 1")

else:
    for i in range(1, num + 1):
        factorial = factorial * i

    print(f"The factorial of {num} is ", factorial)


# factorial of a number by using recursion


def offactorial(n):
    if n == 1:
        return n
    else:
        return n * offactorial(n - 1)


num1 = int(input("Enter your number"))

if num1 < 0:
    print("Ïnvalid request")

elif num1 == 0:
    print("Factorial is 1")

else:
    print(f"factorial of the {num1} is ", offactorial(num1))
