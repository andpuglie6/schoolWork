print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 15, Nov 27, 2017")

class Dog:
    species = 'Canis Lupus Familiaris'
    def __init__(self, nameOne, breedOne):
        self.name = nameOne
        self.breed = breedOne
        self.tricks = []   
        
    def teach(self, trick):
        self.tricks.append(trick)
        print(self.name + " knows " + trick)
        
    def knows(self, trick):
        if trick in self.tricks:
            print("Yes, " + self.name + " knows " + trick)
            print("True")
        else:
            print("No, " + self.name + " doesn't know " + trick)
            print("False")       

