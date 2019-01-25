print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 20, Dec 13, 2017")

#Exercises 1-10 F2015

print('AEEDCABCED')

#Exercise 11A and 11B F2015
'''
import turtle
t = turtle.Turtle()
s = turtle.Screen()

def tri(t, sideLen):
    for i in range(3):
        t.forward(sideLen)
        t.left(120)
        
tri(t, 100)

def tris(t, inital, incr, num, angle):
    for i in range(num):
        tri(t, inital)
        t.left(angle)
        inital += incr
        
tris(t, 20, 50, 5, 60)
'''

#Exercise 12 F2015

import string
'''
def wordsByLine(inFile, outFile):
    firstText = open(inFile, 'r')
    secondText = open(outFile, 'w')
    for line in firstText:
        wordDic = {}
        words = line.strip('\n').lower().split()
        for word in words:
            if word not in wordDic:
                wordDic[word] = 1
            elif word in wordDic:
                wordDic[word] += 1
        secondText.write(str(wordDic))
        secondText.write('\n')
    firstText.close()
    secondText.close()
    
wordsByLine('fish.txt', 'fishWords.txt')
'''

#Exercise 13 F2015

'''     
def lineIndex(fName):
    firstText = open(fName, 'r')
    d = {}
    lineValue = 0
    for line in firstText:
        wordList = line.split()
        for word in wordList:
            if word not in d:
                d[word] = [lineValue]
            elif lineValue not in d[word]:
                d[word] += [lineValue]
        lineValue+=1
    return d

print(lineIndex('makeItRain.txt'))
'''

#Exercises 1-10 S2015

print('BAADDEDCCD')

#Exercise 11A and 11B S2015

'''
import turtle
t = turtle.Turtle()
s = turtle.Screen()

def capT(turt, height):
    turt.left(90)
    turt.forward(height)
    turt.left(90)
    turt.forward(height/4)
    turt.back(height/2)
    turt.forward(height/4)
    turt.left(90)
    turt.forward(height)
    turt.left(90)
    
capT(t, 100)

def tRow(t, num, init, ratio):
    width = init
    for i in range(num):
        t.down()
        capT(t, init)
        t.up()
        t.forward(width)
        init *= ratio

tRow(t, 3, 40, 1.5)
'''

#Exercise 12 S2015

import string
'''
def fileStats(inFile, outFile):
    characterCount = 0
    wordCount = 0
    lineCount = 0
    digitCount = 0
    punctuationCount = 0
    
    digits = '0123456789'
    punctuation = "!$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    firstText = open(inFile, 'r')
    secondText = open(outFile, 'w')
    for line in firstText:
        text = line.split()
        lineCount += 1
        for word in text:
            if word[0] in digits:
                digitCount += len(word)
                characterCount += len(word)
            for char in word:
                if char in punctuation:
                    punctuationCount += 1
                characterCount += 1
            wordCount += 1
    
    secondText.write("characters " + str(characterCount) + "\n" + "words " + str(wordCount) + "\n" + "lines " + str(lineCount) + "\n" + "digits " + str(digitCount) + "\n" + "punctuation " + str(punctuationCount) + "\n")
    
    firstText.close()
    secondText.close()
    
fileStats('fish.txt', 'fishWords.txt')
'''

#Exercise 13 S2015

'''
def symmetry(text):
    d = {}
    textBase = text.lower().split()
    for word in textBase:
        if word[0] == word[-1]:
            if word not in d:
                d[word[0]] = 1
            else:
                d[word[0]] += 1
    return d
'''
t = '''The sun did not shine
it was too wet to play
so we sat in the house
all that cold cold wet day
I sat there with Sally
we sat there we two
and I said how I wish
we had something to do'''
'''
print(symmetry(t))
'''