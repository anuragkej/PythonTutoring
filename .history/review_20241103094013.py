numStr = "3"
num = 34
boolVar = True


if boolVar:
    print("Hello!")

else:
    print("Bye.")

raining = True
while raining:

    print("It's raining.")

    raining = False

# use while loop - boolean (T or F)
# use for loop - incrementing/decrementing (numbers, certain bound)
# for loop printing all odd numbers 1-30 (inclusive)


# functions - bundle a lot of code together


def printOddNumbers(endBound):
    for i in range(1, endBound, 2):
        print(i)


printOddNumbers(21)
print(raining)
