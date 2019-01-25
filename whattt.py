import random
import string
import time
import turtle

class Game:
    def createGame():
        global boardState
        boardState = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        
        global gameScreen
        global gameDraw
        gameScreen = turtle.Screen()
        # gameScreen.setup(1000,600,1,-1)
        gameDraw = turtle.Turtle()
        gameDraw.speed(0)
        gameDraw.penup()
        
        global moveX
        global moveO
        Game.getName()
        
        turn = random.randint(1, 2)
        if turn == 1:
            moveX = "no"
            moveO = "yes"
            print("It is is " + nameO + "'s turn.")
        if turn == 2:  
            moveO = "no"
            moveX = "yes"
            print("It is is " + nameX + "'s turn.")
    
    def drawGrid():
        gameDraw.goto(-300, -300)
        gameDraw.pendown()
        for i in range(4):
            gameDraw.forward(600)
            gameDraw.left(90)
        for i in range(2):
            gameDraw.forward(200)
            gameDraw.left(90)
            gameDraw.forward(600)
            gameDraw.back(600)
            gameDraw.right(90)
        gameDraw.back(400)
        for i in range(2):
            gameDraw.left(90)
            gameDraw.forward(200)
            gameDraw.right(90)
            gameDraw.forward(600)
            gameDraw.back(600)
        gameDraw.right(90)
        gameDraw.forward(400)
        gameDraw.left(90)
    
    def drawX():
        gameDraw.pendown()
        for i in range(2):
            gameDraw.right(45)
            gameDraw.forward(75)
            gameDraw.back(75)
            gameDraw.right(90)
            gameDraw.forward(75)
            gameDraw.back(75)
            gameDraw.right(45)
        gameDraw.penup()

    def drawO():
        gameDraw.penup()
        gameDraw.right(90)
        gameDraw.forward(75)
        gameDraw.left(90)
        gameDraw.pendown()
        gameDraw.circle(75)
        gameDraw.penup()
        
    def getMove():
        if moveX == "yes":
            gameDraw.penup()
            gameDraw.goto(drawSpotX, drawSpotY)
            gameDraw.pendown()
            Game.drawX()
            boardState[integer] = "X"
            
            moveX = "no"
            moveO = "yes"
            
        if moveO == "yes":
            gameDraw.penup()
            gameDraw.goto(drawSpotX, drawSpotY)
            gameDraw.pendown()
            Game.drawO()
            boardState[integer] = "O"
            
            moveO = "no"
            moveX = "yes"
    
    def chooseBox():
        integers = "1 2 3 4 5 6 7 8 9"
        valid = integers.split(" ")
        while True:
            boxNumber = input("Select box 1-9 (starting from the top-left): ")
            if boxNumber not in valid:
                print("Please select a number 1-9")
            else:
                break
        
        global drawSpotX
        global drawSpotY
        global integer
        
        if boxNumber == "1":
            drawSpotX = -200
            drawSpotY = 200
            integer = 0
        elif boxNumber == "2":
            drawSpotX = 0
            drawSpotY = 200
            integer = 1
        elif boxNumber == "3":
            drawSpotX = 200
            drawSpotY = 200
            integer = 2
        elif boxNumber ==  "4":
            drawSpotX = -200
            drawSpotY = 0
            integer = 3
        elif boxNumber == "5":
            drawSpotX = 0
            drawSpotY = 0
            integer = 4
        elif boxNumber == "6":
            drawSpotX = 200
            drawSpotY = 0
            integer = 5
        elif boxNumber == "7":
            drawSpotX = -200
            drawSpotY = -200
            integer = 6
        elif boxNumber == "8":
            drawSpotX = 0
            drawSpotY = 200
            integer = 7
        elif boxNumber == "9":
            drawSpotX = 200
            drawSpotY = -200
            integer = 8

    def getName():
        global nameX
        global nameO
        
        nameX = input("What is player X's name? ")
        nameO = input("What is player O's name? ")


Game.createGame()
Game.drawGrid()
Game.chooseBox()
Game.getMove()