import random
def game():
    winner = 'bot'
    return f'winner: {winner}'

def botChoice(possibleInputs):
    possibleInputs.remove(random.choice(possibleInputs))
    return possibleInputs

def test():
    assert game() == 'winner: you' or game()  == 'winner: bot' or game() == 'tie'
    assert botChoice(['A1']) == []
    assert botChoice(['A1','A2']) == ['A1'] or botChoice(['A1','A2']) == ['A2']