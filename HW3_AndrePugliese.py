print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 03, Sept 20, 2017")

# Exercise 1 and 2

a = 3
b = 4
c = 5

if a < b:
    print("OK")
    
else:
    print("NOT OK")

if c < b:
    print("OK")
    
else:
    print("NOT OK")
    
if a + b == c:
    print("OK")
    
else:
    print("NOT OK")
    
if a**2 + b**2 == c**2:
    print("OK")
    
else:
    print("NOT OK")
    
# Exercise 3

import turtle

color = input("What color? \n")
lineWidth = int(input("How thicc do you want your lines? \n"))
lineLength = int(input("How long do you want your lines? \n"))
shape = input("What shape do you want? \n")

def drawShape(color, lineWidth, lineLength, shape):
    tScreen = turtle.Screen()
    tTurtle = turtle.Turtle()
    
    tTurtle.color(color)
    tTurtle.width(lineWidth)
    
    if shape == "triangle" or shape == "Triangle":
        for i in range(3):
            tTurtle.forward(lineLength)
            tTurtle.left(120);
    if shape == "square" or shape == "Square":
        for i in range(4):
            tTurtle.forward(lineLength)
            tTurtle.left(90);
    if shape == "line" or shape == "Line":
        for i in range(1):
            tTurtle.forward(lineLength)
            
drawShape(color, lineWidth, lineLength, shape)