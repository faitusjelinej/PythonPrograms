class Square:
    def __init__(self,side):
        self.side = side

    def __add__(squareOne,squareTwo):
        return (squareOne.side + squareTwo.side)

squareOne = Square(5)
squareTwo = Square(10)
print("sum of sides", squareOne + squareTwo)


squareOne = Square("Faitus")
squareTwo = Square("Jeline")
print("Name", squareOne + squareTwo)
