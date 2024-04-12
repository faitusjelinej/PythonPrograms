class House:
    def __init__(self,color, owner,location,price):
        self.color = color
        self.owner = owner
        self.location = location
        self.price = price

    def __str__(self):
        return (f"{self.owner} owns the house located in {self.location} painted {self.color} spent {self.price}")    

    def setincrease(self, percentage):
        self.price = self.price + self.price * percentage * .01

    def getincrease(self):
        return self.price
    

owner1 = House("pink","David","NY",1000)
owner2 = House("green","Edward","CA",5000)
owner2.setincrease(5)
owner2.getincrease()

print(owner1)
print(owner2)
