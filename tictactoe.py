import random

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
    gameboard ={
    'A1':'_','A2':'_','A3':'_',
    'B1':'_','B2':'_','B3':'_',
    'C1':'_','C2':'_','C3':'_'}

    gameIsRunning = True
    userTurn = True

    while gameIsRunning == True:
        if userTurn == True:
            isPossibleInput = True
            while isPossibleInput == True:
                userInput = input()
                if userChoice(possibleInputs,userInput) == True:
                    print ('ok')
                    possibleInputs.remove(userInput)
                    gameboard[userInput] = 'X'
                    isPossibleInput = False
            userTurn = False
        else:

            possibleInputs = botChoice(possibleInputs)
            for i in gameboard:
                if i not in possibleInputs:

                    gameboard[i] = 'O'
            userTurn = True
    
        print(printGameBoard(gameboard))

    if decideOutcome(gameboard,'X'):
        return f'winner: you'
    if decideOutcome(gameboard,'O'):
        return f'winner: bot'
    if len(possibleInputs) == 0:
        return f'tie'

    


def test():
    assert game() in ['winner: you', 'winner: bot', 'tie']
    assert botChoice(['A1']) == []
    assert botChoice(['A1','A2']) in [['A1'],  ['A2']]
    assert userChoice(['A1'],'A1') == True
    assert userChoice(['A2'],'A1') == False
    
    gameboard ={
    'A1':'_','A2':'_','A3':'_',
    'B1':'_','B2':'_','B3':'_',
    'C1':'_','C2':'_','C3':'_'}
    assert printGameBoard(gameboard) == f" _ | _ | _ \n"\
                                        f" _ | _ | _ \n"\
                                        f" _ | _ | _ "

    gameboard ={
    'A1':'X','A2':'_','A3':'_',
    'B1':'X','B2':'_','B3':'_',
    'C1':'X','C2':'_','C3':'_'}
    assert printGameBoard(gameboard) == f" X | _ | _ \n"\
                                        f" X | _ | _ \n"\
                                        f" X | _ | _ "

    gameboard ={
    'A1':'X','A2':'_','A3':'_',
    'B1':'X','B2':'_','B3':'_',
    'C1':'X','C2':'_','C3':'_'}
    assert decideOutcome(gameboard,'X') == True

    gameboard ={
    'A1':'_','A2':'O','A3':'_',
    'B1':'_','B2':'O','B3':'_',
    'C1':'_','C2':'O','C3':'_'}
    assert decideOutcome(gameboard,'X') == False
    
    gameboard ={
    'A1':'_','A2':'O','A3':'_',
    'B1':'_','B2':'O','B3':'_',
    'C1':'_','C2':'O','C3':'_'}
    assert decideOutcome(gameboard,'O') == True
    
    gameboard ={
    'A1':'X','A2':'_','A3':'X',
    'B1':'X','B2':'O','B3':'_',
    'C1':'X','C2':'_','C3':'_'}
    assert decideOutcome(gameboard,'X') == True

    gameboard ={
    'A1':'_','A2':'_','A3':'X',
    'B1':'_','B2':'X','B3':'_',
    'C1':'X','C2':'_','C3':'_'}
    assert decideOutcome(gameboard,'X') == True