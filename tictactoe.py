import random
def game():
    possibleInputs = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    gameboard ={
    'A1':'_','A2':'_','A3':'_',
    'B1':'_','B2':'_','B3':'_',
    'C1':'_','C2':'_','C3':'_'}

    winner = 'bot'
    return f'winner: {winner}'

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

    return False


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
    assert userChoice(gameboard,'X') == True