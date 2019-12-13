#!/usr/bin/env python3
# Project 01 - Scrabble Game

# Function 1: Input Player Rounds
def inputRounds():
    try: 
       user_rounds = int(input("Enter Number of Rounds:"))
    except ValueError:
        user_rounds = 2
    except TypeError:
        user_rounds = 2
    return user_rounds

# Function 2: Input Player Word
def inputWord():
    rounds = user_rounds
    while rounds  != 0:
        print('Round ',rounds)
        player1 = input('Player 1 word: ')
        player2 = input('Player 2 word: ')
        players['player1'] = [player1] 
        players['player2'] = [player2] 
        rounds = rounds - 1
    else:
        return players['player1'], players['player2']

# Function 3: Validate Word
def validWord():
    return None

# Function 4: Generate Score
def playerScore():
    return None

# Function 5: Initialize Messages Tuple
def initMessages():
    return None

# Function 6: Initialize Points Dictionary
def initPoints():
    return None

# Function 7: Initialize Players Dictionary
def initPlayers():
    players = { 'rounds':0, 
                'player1':[], 
                'player2':[], 
                'score1':0, 
                'score2':0 }
    return players

# Main Program
if __name__ == '__main__':

    # Declare Variables
    points = initPoints()
    players = initPlayers()
    messages = initMessages()
    user_rounds = inputRounds()
    player1_word , player2_word = inputWord()
   

    # Main Program
    #print('Main Program Goes Here')
    print(players)
    
    