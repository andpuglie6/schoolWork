print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 08, Oct 9, 2017")

# Questions 1 - 10
# E B C D C A C A B (Question Mark)E

# Questions 11A

import turtle
t = turtle.Turtle()
s = turtle.Screen()

def drawSquare(t, length):
    for i in range(4):
        t.forward(length)
        t.right(90)
'''  
drawSquare(t, 100)
'''
# Questions 11B

def drawSquares(t, size, num, angle):
    for i in range(num):
        drawSquare(t, size)
        t.right(angle)
        
drawSquares(t, 100, 10, 10)

# Questions 12

def bigCount(numList, threshold):
    count = 0
    for i in numList:
        if i > threshold:
            count += 1
        
    return count

someNums = [-5, 6, 3, 0, 7]
print(bigCount(someNums, 2))

# Questions 13

def getDate(message):
    month = str(input("What month is it?\n"))
    day = int(input("What day is it?\n"))
    print(month + " " + str(day) + " " + message)
    return str(month + " " + str(day))
    
today = getDate("is a great day!")
print(today)