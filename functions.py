# def add(int1):
#     print(int1)


# create a function that takes in a random number
# and prints it out
import random

# randIntParam = random.randint(1, 100)

# def randomNumber(randomInt):
#     print(randomInt)

# randomNumber(randIntParam)

# create a magic 8 ball game function
# that uses random and conditionals


randIntParam = random.randint(1, 5)


def magic8Num(randomInt):
    print(randomInt)
    if randomInt == 1:
        print("I don't know.")

    if randomInt == 2:
        print("Yes, You are right.")

    if randomInt == 3:
        print("No, I don't think so.")

    if randomInt == 4:
        print("I will tell you later. This might not be the best time.")

    if randomInt == 5:
        print("You must figure it out yourself.")


magic8Num(randIntParam)
