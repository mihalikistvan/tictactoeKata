def game():
    winner = 'bot'
    return f'winner: {winner}'

def botChoice(possibleInputs):
    return False

def test():
    assert game() == 'winner: you' or game()  == 'winner: bot' or game() == 'tie'
    assert botChoice(['A1']) ==[]