import random


class TennisRacket:
    # color
    # Brand
    # Size

    # constructor
    def __init__(self, color, handleColor, size, brand):
        self.color = color
        self.handleColor = handleColor
        self.size = size
        self.brand = brand
        self.points = 0

    def changeColor(self, newColor):
        self.color = newColor

    def changeSize(self, newSize):
        self.size = newSize

    # create a function that simulates real time gameplay, use random to show how many games we would win
    def play(self, numGames):
        gamesWon = random.randint(0, numGames)
        self.points += gamesWon
        return gamesWon

    def serves(self, serveList):
        typeOfServe = random.randint(0, len(serveList) - 1)
        return serveList[typeOfServe]


wilsonRacket = TennisRacket("Red", "White", 5, "Wilson")

AaravRacket = TennisRacket("Black", "Green", 7, "Aarav")

AaravRacket.changeSize(26)
gamesWon = AaravRacket.play(7)
print(AaravRacket.points)

typeOfServes = ["Topspin", "Kick", "Flat", "Underhand"]
print(AaravRacket.serves(typeOfServes))

wilsonRacket.changeColor("White")

# print(wilsonRacket.color)


# hi = TennisRacket("Yellow", 5, "Wilson")
# bye = TennisRacket("Blue", 5, "Wilson")
# anurag = TennisRacket("Green", 5, "Wilson")
