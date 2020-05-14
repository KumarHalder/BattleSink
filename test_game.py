from player import player
from gameManager import  gameManager
'''
Test player.py FileExistsError
'''
def test_placeShip_shipPosition():
    playerTest = player("playerTest")
    playerTest.placeShip(1,0,True)
    assert playerTest.opponentShipCoordinates == [[0,0],[1,0],[2,0]]


def test_placeShip_edgeCases():
    playerTest = player("playerTest")
    assert playerTest.placeShip(0,0,True) == False and playerTest.placeShip(7,0,True) == False  and playerTest.placeShip(0,7,True) == False


def test_isOpponentShipAtPosition():
    playerTest = player("playerTest")
    playerTest.placeShip(1, 0, True)
    assert playerTest.isOpponentShipAtPosition(1,0) == True and playerTest.isOpponentShipAtPosition(3,0) == False

def test_shotPoint():
    playerTest = player("playerTest")
    playerTest.placeShip(1, 0, True)
    playerTest.shotPoint(1,0)
    assert playerTest.opponentHealth == 2 and playerTest.opponentBoard[0][1] == 'hit'

def test_isThisMoveUSedPreviously():
    playerTest = player("playerTest")
    playerTest.shotPoint(1,1)
    assert playerTest.isThisMoveUSedPreviously(1,1) == True and playerTest.isThisMoveUSedPreviously(2,1) == False

def test_opponentBeenShot():
    playerTest = player("playerTest")
    playerTest.opponentBeenShot()
    assert playerTest.opponentHealth == 2

def test_opponentDestroyed():
    playerTest = player("playerTest",0)
    assert playerTest.opponentDestroyed() == True

'''
Test gameManager.py FileExistsError
'''
def test_setPlayerTurn():
    game = gameManager()
    game.turn = 1
    game.player1.placeShip(1,0,True)
    assert game.setPlayerTurn() == "Player2 turn: "

def test_firedAtPosition():
    game = gameManager()
    game.player1.placeShip(1, 0, True)
    game.player2.placeShip(1, 0, True)
    game.firedAtPosition('B','1')
    game.turn += 1
    game.setPlayerTurn()
    game.firedAtPosition('D', '1')
    assert game.player1.opponentBoard[game.verticalMove['1']][game.horizontalMove['B']] == 'hit' and game.player2.opponentBoard[game.verticalMove['1']][game.horizontalMove['D']] == 'X'

def test_isThisMoveUSedPreviously():
    game = gameManager()
    game.firedAtPosition('B', '1')
    print('isthismoveusedprev')
    assert game.isThisMoveUSedPreviously(1,0) == True

def test_isValidMove():
    game = gameManager()
    assert game.isValidMove('A','2') == True and game.isValidMove('L','2') == False and game.isValidMove('A','9') == False

def test_isGameOver():
    game = gameManager()
    game.player2.opponentHealth = 0
    assert game.isGameOver() == True




