class Apple: #base class
    manufacturer = "Apple Inc."
    contactWebsite = "Apple.com/contact"

    def contactdetails(self):
        print("To contact us login to",self.contactWebsite)

class Macbook(Apple): # derived class
    def __init__(self):
        self.yearofmanufacture = 2017

    def manufacturerdetails(self):
        print("This product was manufactued in {} by {}".format(self.yearofmanufacture,self.manufacturer))


Macbook = Macbook()
Macbook.manufacturerdetails()
Macbook.contactdetails()
