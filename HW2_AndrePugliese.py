print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 02, Sept 18, 2017")

# Exercise 1

import turtle
aScreen = turtle.Screen()
aTurtle = turtle.Turtle()
lineLength = 100

def drawShape(length):
    for i in range(3):
        aTurtle.forward(length)
        aTurtle.left(120);
    for i in range(4):
        aTurtle.forward(length)
        aTurtle.left(90);
    for i in range(5):
        aTurtle.forward(length)
        aTurtle.left(72);
        
drawShape(lineLength)

# Exercise 2

for i in range(50, 250, 50):
    aTurtle.penup()
    aTurtle.right(90)
    aTurtle.forward(i)
    aTurtle.left(90)
    aTurtle.pendown()
    aTurtle.circle(i)
    aTurtle.penup()
    aTurtle.home()

# Exercise 3

import math
print(math.factorial(100))

print(math.log2(1000000))

print(math.gcd(63, 49))