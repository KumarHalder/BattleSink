from board import board

print(".......RULES OF GAME.............")
print("two player game, each plaeyr takes turn after another")
print("first turn is for placing ships by each player, it takes three arguments of space separated value,\n"
      "where first two are coordinates of the ship center, and the last is H/V, providing the placement of \nthe ship"
      "horizontally or vertically (exp: 2 2 H)")
print("after placement, each player guesses and fires by coordinates in space separated values (exp: 2 2)")
print(".........Lets have fun ........\n\n\n")


player1 = board("player1")
player2 = board("player2")

turn = 0
player1turn=True

x1, y1, isHorizontal1 = input("Player1 ship position: x:int,  y:int , H/V: str : ").split()
while(player2.placeShip(int(x1),int(y1),isHorizontal1=="H") == False):
    x1, y1, isHorizontal1 = input("Player1 ship position: x:int,  y:int , H/V: str : ").split()
    #player2.placeShip(int(x1), int(y1), isHorizontal1 == "H")

x2, y2, isHorizontal2 = input("Player2 ship position: x:int,  y:int , H/V: str : ").split()
while(player1.placeShip(int(x2),int(y2),isHorizontal2=="H") == False):
    x2, y2, isHorizontal2 = input("Player2 ship position: x:int,  y:int , H/V: str : ").split()
    #player1.placeShip(int(x2), int(y2), isHorizontal2 == "H")

def setPlayerTurn():
    global turn,player1turn

    print("turnCount: ",turn)
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

def isThisMoveUSedPreviously(x,y):

    if player1turn:
        return player1.isThisMoveUSedPreviously(x,y)
    else:
        return player2.isThisMoveUSedPreviously(x, y)

def isValidMove(x,y):
    if (x > 7 or x < 0 or y > 7 or y < 0):
        return False
    elif isThisMoveUSedPreviously(x,y):
        return False
    return True

def isGameOverBetween(player1,player2):
    if (player1.opponentDestroyed() or player2.opponentDestroyed()) == True:
        print("..........Game Over..........")
        return True
    return False

while(isGameOverBetween(player1,player2) == False):
    print(setPlayerTurn())
    x,y = input("fire at position x y : ").split()
    x,y = int(x),int(y)
    if isValidMove(x,y) :
       firedAtPosition(x,y)
    else:
        while isValidMove(x,y)==False:
            print("Invalid Move, please try again, possible cause - out of board position/previously same used position")
            x, y = input("fire at position x y : ").split()
            x, y = int(x), int(y)





