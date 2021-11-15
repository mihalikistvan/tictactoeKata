import random
import time
def botChoice(possibleInputs):
    possibleInputs.remove(random.choice(possibleInputs))
    return possibleInputs

def userChoice(possibleInputs,choice):
    if choice in possibleInputs:
        return True
    else:
        return False

def printGameBoard(dataSet):
    return  f" {dataSet['A1']} | {dataSet['A2']} | {dataSet['A3']} \n"\
            f" {dataSet['B1']} | {dataSet['B2']} | {dataSet['B3']} \n"\
            f" {dataSet['C1']} | {dataSet['C2']} | {dataSet['C3']} "

def decideOutcome(gameBoard,mark):
    possibleWins = {
       1:['A1','A2','A3'],
       2:['B1','B2','B3'],
       3:['C1','C2','C3'],
       4:['A1','B1','C1'],
       5:['A2','B2','C2'],
       6:['A3','B3','C3'],
       7:['A1','B2','C3'],
       8:['A3','B2','C1'] 
    }
    for possibleWin in possibleWins:
        if gameBoard[possibleWins[possibleWin][0]] == gameBoard[possibleWins[possibleWin][1]] == gameBoard[possibleWins[possibleWin][2]] == mark:
            return True
    return False

def game():
    possibleInputs = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']

    helper={
            'A1':'A1','A2':'A2','A3':'A3',
            'B1':'B1','B2':'B2','B3':'B3',
            'C1':'C1','C2':'C2','C3':'C3'}
    print ('the gameboard')
    print(printGameBoard(helper))
    gameboard ={
    'A1':'_','A2':'_','A3':'_',
    'B1':'_','B2':'_','B3':'_',
    'C1':'_','C2':'_','C3':'_'}

    gameIsRunning = True
    userTurn = True
    print ('start of game')
    while gameIsRunning:
        time.sleep(2)
        if userTurn:
            isPossibleInput = True
            while isPossibleInput:
                print ('please insert a coordinate')
                userInput = input()
                if userChoice(possibleInputs,userInput):
                    possibleInputs.remove(userInput)
                    gameboard[userInput] = 'X'
                    isPossibleInput = False
                else:
                    print ('not valid')
            userTurn = False
        else:
            print()
            print ('bots choice:')
            possibleInputs = botChoice(possibleInputs)
            for i in gameboard:
                if i not in possibleInputs:
                    if gameboard[i] not in ['X','O']: 
                        gameboard[i] = 'O'
            userTurn = True
    
        print(printGameBoard(gameboard))

        if decideOutcome(gameboard,'X'):
            gameIsRunning = False
            return f'winner: you'
        if decideOutcome(gameboard,'O'):
            gameIsRunning = False
            return f'winner: bot'
        if len(possibleInputs) == 0:
            gameIsRunning = False
            return f'tie'


def game2():
    possibleInputs = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']

    helper={
            'A1':'A1','A2':'A2','A3':'A3',
            'B1':'B1','B2':'B2','B3':'B3',
            'C1':'C1','C2':'C2','C3':'C3'}
    print ('the gameboard')
    print(printGameBoard(helper))
    gameboard ={
    'A1':'_','A2':'_','A3':'_',
    'B1':'_','B2':'_','B3':'_',
    'C1':'_','C2':'_','C3':'_'}

    gameIsRunning = True
    bot1Turn = True
    print ('start of game')
    while gameIsRunning:
        time.sleep(2)
        if bot1Turn:
            print()
            print ('bot1 choice:')
            possibleInputs = botChoice(possibleInputs)
            for i in gameboard:
                if i not in possibleInputs:
                    if gameboard[i] not in ['X','O']: 
                        gameboard[i] = 'X'
            bot1Turn = False
        else:
            print()
            print ('bot2 choice:')
            possibleInputs = botChoice(possibleInputs)
            for i in gameboard:
                if i not in possibleInputs:
                    if gameboard[i] not in ['X','O']: 
                        gameboard[i] = 'O'
            bot1Turn = True
    
        print(printGameBoard(gameboard))

        if decideOutcome(gameboard,'X'):
            gameIsRunning = False
            return f'winner: bot1'
        if decideOutcome(gameboard,'O'):
            gameIsRunning = False
            return f'winner: bot2'
        if len(possibleInputs) == 0:
            gameIsRunning = False
            return f'tie'


print(game2())