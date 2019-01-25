print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 05, Sept 27, 2017")

# Exercise 1A

def hasFinalLetter(strList, letters):
    contain = []
    for a in strList:
        for p in letters:
            if a[-1] == p:
                contain.append(a)
                
    return contain
             
strList = ["ball", "boat", "bear", "balloon", "beet"]
letters = ["l", "t"]
print(hasFinalLetter(strList, letters))

# Exercise 1B

# Empty List
dogs = ["german shepherd", "rottweiler", "st. bernard"]
lettersOne = ["z", "b"]

print(hasFinalLetter(dogs, lettersOne))

# Half Filled Condition

muppets = ["Elmo", "Big Bird", "Oscar the Grouch", "Grover"]
lettersTwo = ["d", "y"]

print(hasFinalLetter(muppets, lettersTwo))

# Filled Condition

dinosaurs = ["Tyrannosaurus", "Triceratops", "Stegosaurus", "Velociraptor"]
lettersThree = ["s", "r"]

print(hasFinalLetter(dinosaurs, lettersThree))

# Exercise 2A

def isDivisible(maxInt, twoInts):
    rand = []
    for i in range(maxInt):
        if i%twoInts[0]  == 0 and i%twoInts[1] == 0:
            rand.append(i)
            
    return(rand)
    
maxInt = 40
twoInts = (2, 4)

print(isDivisible(maxInt, twoInts))

# Exercise 2B
    
maxIntOne = 300
twoIntsOne = (2, 9)

print(isDivisible(maxIntOne, twoIntsOne))

maxIntTwo = 271
twoIntsTwo = (7, 9)

print(isDivisible(maxIntTwo, twoIntsTwo))

# You cannot return an empty list as one will always contain 0.
