class musicalinstruments:
    numberofmajorkeys = 12

class stringinstruments(musicalinstruments):
    typeofwood = "Tone wood"

class Guitar(stringinstruments):
    def __init__(self):
        self.numberofstrings = 6
        print("This guitar consists of {} strings. It is madeup of {}. It has {} major keys.".format(self.numberofstrings,self.typeofwood,self.numberofmajorkeys))


guitar = Guitar()
