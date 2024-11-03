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

    def changeColor(self, newColor):
        self.color = newColor


wilsonRacket = TennisRacket("Red", "White", 5, "Wilson")

# wilsonRacket.changeColor("White")

print(wilsonRacket.color)


# hi = TennisRacket("Yellow", 5, "Wilson")
# bye = TennisRacket("Blue", 5, "Wilson")
# anurag = TennisRacket("Green", 5, "Wilson")
