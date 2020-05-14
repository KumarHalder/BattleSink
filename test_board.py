from player import player


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

