import random
def game():
    possibleInputs = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
    winner = 'bot'
    return f'winner: {winner}'

def botChoice(possibleInputs):
    possibleInputs.remove(random.choice(possibleInputs))
    return possibleInputs

def userChoice(possibleInputs,choice):
    return False
    
def test():
    assert game() == 'winner: you' or game()  == 'winner: bot' or game() == 'tie'
    assert botChoice(['A1']) == []
    assert botChoice(['A1','A2']) == ['A1'] or botChoice(['A1','A2']) == ['A2']
    assert userChoice(['A1'],'A1') == True