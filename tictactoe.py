def game():
    winner = 'bot'

    return f'winner: {winner}'



def test():
    assert game() == 'winner: you' or game()  == 'winner: bot' or game() == 'tie'