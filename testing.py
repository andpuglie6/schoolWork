print("#Andre Pugliese")
print("#CS 100-H01")
print("#HW 09, Oct 17, 2017")

# Question 1

def twoWords(length, firstLetter):  
    while True:
        firstWord = input("Enter a" + " " + str(length)  + "-letter word please ")
        
        if len(firstWord) == length:
            secondWord = input("Enter a word beginning with " + firstLetter  + " please ")
            
            if secondWord[0] == firstLetter:
                break
            if secondWord[0] != firstLetter:
                continue
                
        if len(firstWord) != length:
            continue
        
twoWords(4, "B")

# Question 2

def twoWordsV2(length, firstLetter):
    matchOne = False
    
    while matchOne != True:
        firstWord = input("Enter a" + " " + str(length)  + "-letter word please ")
        if len(firstWord) == length:
            matchOne = True
            
            matchTwo = False
            while matchTwo != True:
                secondWord = input("Enter a word beginning with " + firstLetter  + " please ")
                if secondWord[0] == firstLetter:
                    matchTwo = True
        
twoWordsV2(4, "B")

# Question 3

def count_digit(a):
    sum = 0
    for i in range(10):
        sum += a.count(str(i))
    return sum

def enterNewPassword():
    maxChar = 15
    minChar = 8
    
    while True:
        password = (input("Enter a new password between 8-15 characters in length. It must also include 1 digit.\n"))
        isDigit = count_digit(password)
        
        if len(password) > maxChar and isDigit >= 1:
            print("Your password is too long. Please use another.")
            continue
        if len(password) > maxChar and isDigit < 1:
            print("Your password is too long. You do not have a digit in your password. Please use another.")
            continue
        if len(password) < minChar and isDigit >= 1:
            print("Your password is too short. Please use another.")
            continue
        if len(password) < minChar and isDigit < 1:
            print("Your password is too short. You do not have a digit in your password. Please use another.")
            continue
        if len(password) >= minChar and len(password) <= maxChar and isDigit >= 1:
            print("Password Accepted. Thank you.")
            break
        
enterNewPassword()


def guessNumberGame():
    import random
    guessCount = 1
    maxGuess = 5
    number = int(random.randint(0, 50))
    print("I’m thinking of a number in the range 0-50. You have five tries to guess it.\n")
    
    while True:
        guess = input("Guess " + str(guessCount) +"? ")
 
        if int(guessCount) == 5:
            print("You lose! I was thinking of " + str(number) + "!")
            break
        if guess == '':
            continue
        if int(guess) > number:
            print(str(guess) + " is too high.")
            guessCount += 1
            continue
        if int(guess) < number:
            print(str(guess) + " is too low.")
            guessCount += 1 
            continue
        if int(guess) == number:
            print("You are right! I was thinking of " + str(number) + "!")
            break

guessNumberGame()
        
        