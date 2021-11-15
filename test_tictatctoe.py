from tictactoe import *
def test():
    #assert game() in ['winner: you', 'winner: bot', 'tie']
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