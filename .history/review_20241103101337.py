import random

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


for j in range(2, 5):
    print(j)

# printOddNumbers(21)

# accessing by index
# serves = [[3, 4], [5, 4], [0, 2]]
# randServe = random.randint(0, 2)

# print(serves[randServe])


# we can basicalyl pick random RPS for 2 players, repeat this numTimes
def rockPaperScissors(numTimes):
    # size of choices = 3, last index is 3 - 1: 2
    choices = ["Rock", "Paper", "Scissors"]

    for a in range(numTimes):
        # set players to either RPS
        player1 = choices[random.randint(0, len(choices) - 1)]
        player2 = choices[random.randint(0, len(choices) - 1)]

    # print(choices[randomChoice])
