import random
from itertools import permutations

def bagelResult(number, guess):
    fc = 0
    bc = 0
    pc = 0
    for i in range(len(guess)):
        if guess[i] == number[i]:
            fc += 1
        elif guess[i] in number:
            pc += 1
        else:
            bc += 1
    return [fc, pc, bc]

def cbagels():
    print("My program is playing Bagels!\n")
    validNums = '0123456789'
    randomNumber = ''
    
    for i in range(3):
        number = random.randint(0, 9)
        randomNumber += str(number)
    randomNumber = '333'
    tryCount = 0
    duplicateNum = -1
    fermiCount = 0
    
    for num in validNums:
        clue = bagelResult(randomNumber, num*3)
        if clue[2] == 3:
            validNums = validNums.replace(num, '')
        elif clue[0] == 1:
            fermiCount += 1
        elif clue[0] == 2:
            duplicateNum = num
        elif clue[0] == 3:
            return "Tries: " + str(tryCount) + "\n" + "Correct Number: " + num*3
        tryCount += 1
        if fermiCount == 3:
            validNums = validNums.replace(validNums[validNums.find(num)+1:], '')
            break
        
    guessedNumber = ''
    if len(validNums) == 1:
        return "Tries: " + str(tryCount) + "\n" + "Correct Number: " + validNums
    
    elif len(validNums) == 2:
        l = list(permutations(validNums + duplicateNum))
        for guessList in l:
            guessedNumber = ''
            for num in guessList:
                guessedNumber += num
            guessResult = bagelResult(randomNumber, guessedNumber)
            tryCount += 1
            if guessResult[0] == 3:
                return "Tries: " + str(tryCount) + "\n" + "Correct Number: " + str(guessedNumber)
    
        
    elif len(validNums) == 3:
        l = list(permutations(validNums))
        for guessList in l:
            guessedNumber = ''
            for num in guessList:
                guessedNumber += num
            guessResult = bagelResult(randomNumber, guessedNumber)
            tryCount += 1
            if guessResult[0] == 3:
                return "Tries: " + str(tryCount) + "\n" + "Correct Number: " + str(guessedNumber)
    
print(cbagels())
    
'''
Test Case I:

Input : Random Generated Int(027)
Output: Tries: 9
        Correct Number: 027
        
Test Case II:

Input : Random Generated Int(333)
Output: Tries: 3
        Correct Number: 333
        
Test Case III:

Input : Random Generated Int(220)
Output: Tries: 14
        Correct Number: 027
        
Note: The minimum number of tries woul;d be 1 if the number was '000' and the maximum number of tries would be at most 16.
'''