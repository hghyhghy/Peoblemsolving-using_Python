# printing all prime numbers in an interval

lower = 900

upper = 1000


print("Prime numbers between ", lower, "and ", upper, "is")

# creating a for loop

for num in range(lower, upper + 1):
    # checking wheather the number is less than 1

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)
