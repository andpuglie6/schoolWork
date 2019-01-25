import random
import string

class Game:
    def makeSecret(player1):
        ''' Return a three character string composed of random digits (000-999).'''
        if player1 == 'human':
            return HumanPlayer.getHumanGuess()
        else:  
            secret = ''
            for i in range(3):
                secret += random.choice(string.digits)
            ComputerPlayer.secretHistory.append(secret)
            return secret
        
    def getClues(secret, guess):
        ''' In a game of bagels, given

        secret -- a three character string of digits 
        guess  -- a three character string of digits

        calculate and return a three-tuple of clues (fermis, picos, bagels).

        A fermi is a guess digit that matches the secret in value and position.
        A pico is a guess digit that matches a secret digit in value but not in
        position. A bagel is a guess digit that does not match a secret digit.

        Each guess digit may match at most one secret digit, and is assigned
        exactly one clue. Each secret digit may match at most one guess digit.
        '''
        fermis = picos = bagels = 0

        ''' Record whether each digit in secret has been matched with a digit
            in guess'''
        matched = [False, False, False]

        ''' Count fermis '''
        for i in range(3):              
            if guess[i] == secret[i]:  
                matched[i] = True
                fermis += 1
                
        ''' Count picos '''
        for guessIdx in range(3):
            for secretIdx in range(3):
                ''' Guess digit must be in different position than secret digit '''
                if guessIdx == secretIdx: 
                    continue              

                ''' Secret digit must not already be matched '''
                if matched[secretIdx] == True: 
                    continue                   
                
                if guess[guessIdx] == secret[secretIdx]: 
                    matched[secretIdx] = True
                    picos += 1
                    break  

        ''' Each guess digit gets a clue, so clues add up to 3 '''
        bagels = 3-fermis-picos
        return (fermis, picos, bagels)
        
    def playBagels(player1, player2):
        ''' Play a single game of bagels:

            i.   create a secret three digit string
            ii.  loop, getting a 3 digit guess from player2 on each iteration
            iii. for each guess, get the clues as a (f,p,b) tuple
            iv.  for each guess, print the clues for player2 if player2 is human
            iii. maintain global guessHistory and clueHistory lists that
                 may be accessed by player2 (if Player2 is a computer function)

            When player2 guesses the secret, print and return the guess count.
        '''
        #global guessHistory, clueHistory
        ComputerPlayer.populateSecretSpace()
        secret = Game.makeSecret(player1)
        #guessHistory = []
        #clueHistory = []

        print('Secret', secret, end='. ')

        while True:
            if player2 == 'human':
                guess = HumanPlayer.getHumanGuess()
            elif player2 == 'randomPlayer':
                guess = Game.makeSecret('computer')
            elif player2 == 'filterPlayer':
                guess = random.choice(ComputerPlayer.secretSpace)
                print(guess)

            ComputerPlayer.guessHistory.append(guess)

            clues = Game.getClues(secret, guess)
            ComputerPlayer.clueHistory.append(clues)
            ComputerPlayer.pruneSecretSpace()

            if player2 == 'human':
                print('For', guess, 'the clues (f/p/b) are', clues)

            if guess == secret:
                print('Guessed', secret, 'in', len(ComputerPlayer.guessHistory), 'guesses!')
                return len(ComputerPlayer.guessHistory)

    def playBagelsSeries(player1, player2, numGames):
        ''' Play a series (numGames) games of bagels. player1 is either
            'computer' or 'human'. player2 is 'human', 'randomPlayer'
            (computer) or 'filterPlayer' (computer).'''
        numGuesses = [] # for each game

        for i in range(numGames):
            print('Game', i, end='. ')
            numGuesses.append(Game.playBagels(player1, player2))

        print(numGames, 'games')
        print('min', min(numGuesses))
        print('max', max(numGuesses))
        print('average', sum(numGuesses)/numGames)

class HumanPlayer:
    def getHumanGuess():
        ''' Input a three character guess in the range [000-999] from
            the (human) user and return it
        '''
        while True:
            guess = input('Your three digit number please (000-999): ')
            
            if len(guess) != 3:
                print('Your number must have exactly 3 digits')
                continue

            ''' Check if there is a nondigit in guess '''
            nondigit = False
            for char in guess:
                if char not in string.digits:
                    nondigit = True
                    break
            if nondigit == True:
                 print('Digits only')
                 continue
            
            return guess
    
class ComputerPlayer:
    secretHistory = []
    guessHistory = []
    clueHistory = []
    secretSpace = []
    def populateSecretSpace():
        ''' populate space of possible secrets with strings 000-999 '''
        #global secretSpace
        for i in string.digits:
            for j in string.digits:
                for k in string.digits:
                    ComputerPlayer.secretSpace.append(i+j+k)


    def pruneSecretSpace():
        ''' remove all secrets from secretSpace that yield a different
            set of clues when tested against the most recent guess'''
        #global secretSpace
        lastGuess = ComputerPlayer.guessHistory[-1]
        lastClue = ComputerPlayer.clueHistory[-1]
        newSpace = []
        for element in ComputerPlayer.secretSpace:
            if Game.getClues(element, lastGuess) == lastClue:
                newSpace.append(element)
        ComputerPlayer.secretSpace = newSpace
 
#Game.playBagelsSeries('human', 'human', 1)
#Game.playBagelsSeries('computer', 'filterPlayer', 100)
#Game.playBagelsSeries('human', 'filterPlayer', 10)