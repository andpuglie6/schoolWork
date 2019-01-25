print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 19b, Dec 10, 2017")

#Exercises 1-10 F2016

print("BCEADACBED")

#Exercise 11A and 11B F2016
'''
import turtle
t = turtle.Turtle()
s = turtle.Screen()

def regularPoly(t, sideLen, numSides):
    for i in range(numSides):
        t.forward(sideLen)
        t.left(360/numSides)
        
regularPoly(t, 100, 6)

def regularPolys(t, sideLen, initialSide, maxSides):
    currentSide = initialSide
    for i in range(maxSides - initialSide + 1):
        regularPoly(t, sideLen, currentSide)
        currentSide += 1
        
regularPolys(t, 100, 3, 8)

#Exercise 12 F2016

import string

def wordLengths(inFile, outFile):
    firstText = open(inFile, 'r')
    secondText = open(outFile, 'w')
    for line in firstText:
        longestLength = 0
        sameLength = 0
        wordList = line.split()
        for word in wordList:
            if len(word) > longestLength:
                longestLength = len(word)
                sameLength = 0
            if len(word) == longestLength:
                sameLength += 1
        secondText.write(str(longestLength) + " " + str(sameLength) + "\n")
        
    firstText.close()
    secondText.close()

wordLengths('zax.txt', 'zaxOut.txt')

#Exercise 13A and 13B F2016

import string

def countVowels(s):
    vowels = 'aeiou'
    text = s.lower()
    vowelCount = 0
    for letter in text:
        if letter in vowels:
            vowelCount += 1
    return vowelCount

print(countVowels('Amen'))

def vowelFrequency(t):
    vowels = 'aeiou'
    text = t.lower().split()
    wordDictionary = {}
    for word in text:
        vowelCount = 0
        for letter in word:
            if letter in vowels:
                vowelCount += 1
        if vowelCount not in wordDictionary:
            wordDictionary[vowelCount] = [word]
        elif word in wordDictionary[vowelCount]:
            continue
        else:
            wordDictionary[vowelCount] += [word]
    
    return wordDictionary

text = "Where hunger is ugly where souls are forgotten"
print(vowelFrequency(text))
  
      '''  

#Exercises 1-10 S2017

print("EBEDBBDEEA")

#Exercises 11A and 11B S2017
'''
import turtle
t = turtle.Turtle()
s = turtle.Screen()

def halfSquare(t, length):
    for i in range(2):
        t.forward(length)
        t.left(90)
'''

'''
halfSquare(t, 100)
'''

'''
def spiral(t, increment, num):
    initiallength = increment
    for i in range(num):
        halfSquare(t, initiallength)
        initiallength += increment

spiral(t, 20, 10)
'''
#Exercises 12 S2017

'''
import string

def wordLengths(inFile, outFile):
    firstText = open(inFile, 'r')
    secondText = open(outFile, 'w')
    for line in firstText:
        uniqueCharacters = 0
        uniqueWords = 0
        uniqueCharacterList = []
        uniqueWordList = []
        
        characterList = line.lower().strip("\n")
        for char in characterList:
            if char not in uniqueCharacterList:
                uniqueCharacterList.append(char)
            else:
                continue
        uniqueCharacters += len(uniqueCharacterList)
        worldList = line.lower().split()
        for word in worldList:
            if word not in uniqueWordList:
                uniqueWordList.append(word)
            else:
                continue
        uniqueWords += len(uniqueWordList)
        secondText.write("words " + str(uniqueWords) + " chars " + str(uniqueCharacters) + "\n")
        
    firstText.close()
    secondText.close()

wordLengths('zax.txt', 'zaxOut.txt')
'''

#Exercise 13 S2017

def vowelEndings(text):
    vowels = 'aeiou'
    vowelDic = {}
    useText = text.lower().split()
    for word in useText:
        if word[-1] in vowels:
            if word[-1] not in vowelDic:
                vowelDic[word[-1]] = [word]
            elif word not in vowelDic[word[-1]]:
                vowelDic[word[-1]] += [word]
            else:
                continue
            
    return vowelDic

t = 'today you are you there is no one alive who is you-er than you'
print(vowelEndings(t))