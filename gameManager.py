from board import board

player1 = board()
player2 = board()

turn = 0
player1turn=True


def setPlayerTurn():
    global turn,player1turn

    print(turn)
    if turn % 2 == 0:
        turn += 1
        player1turn = True
        return "Player1 turn: "
    turn += 1
    player1turn = False
    return "Player2 turn: "

def firedAtPosition(x,y):

    if player1turn:

        player1.shotPoint(x,y)
    else:

        player2.shotPoint(x, y)

while(True):
    print(setPlayerTurn())
    print(player1turn, "player1")
    x,y = input("fire at position x y : ").split()
    x,y = int(x),int(y)
    firedAtPosition(x,y)



print(player1.ownShip)
print(player2.ownShip)

