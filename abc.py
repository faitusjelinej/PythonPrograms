from abc import abstractmethod, ABCMeta


class Shapes(metaclass = ABCMeta):  #abstract base class does not have def on its own
    def area(self):
        return 0

class Square(Shapes):
    side = 5
    def area(self):
        print("Area of Square is : ", self.side * self.side)

class Rectangle(Shapes):
    width = 10
    lenght = 30
    def area(self):
        print("Area of Square is : ", self.width * self.lenght)

square = Square()
square.area()

rectangle = Rectangle()
rectangle.area()
