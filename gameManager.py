from player import player

print(".......RULES OF GAME.............")
print("two player game, each plaeyr takes turn after another")
print("first turn is for placing ships by each player, it takes three arguments of space separated value,\n"
      "where first two are coordinates of the ship center, and the last is H/V, providing the placement of \nthe ship"
      "horizontally or vertically (exp: 2 2 H)")
print("after placement, each player guesses and fires by coordinates in space separated values (exp: 2 2)")
print(".........Lets have fun ........\n\n\n")

class gameManager:
    def __init__(self):
        self.player1 = player("player1")
        self.player2 = player("player2")
        self.turn = 0
        self.player1turn = True
        self.horizontalMove = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.verticalMove = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}


    def playerPlaceShip(self,player:player):
        x, y, isHorizontal1 = input(str(player.name)+" ship position: x:int,  y:int , H/V: str : ").split()
        while (self.player.placeShip(self.horizontalMove[x], self.verticalMove[y], isHorizontal1 == "H") == False):
            x, y, isHorizontal = input("Player1 ship position: x:int,  y:int , H/V: str : ").split()


    #player2.placeShip(int(x1), int(y1), isHorizontal1 == "H")

x2, y2, isHorizontal2 = input("Player2 ship position: x:int,  y:int , H/V: str : ").split()
while(player1.placeShip(horizontalMove[x2],verticalMove[y2],isHorizontal2=="H") == False):
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
    #x,y = int(x),int(y)
    if isValidMove(horizontalMove[x],verticalMove[y]) :
       firedAtPosition(horizontalMove[x],verticalMove[y])
    else:
        while isValidMove(horizontalMove[x],verticalMove[y])==False:
            print("Invalid Move, please try again, possible cause - out of board position/previously same used position")
            x, y = input("fire at position x y : ").split()
            #x, y = int(x), int(y)
        firedAtPosition(horizontalMove[x], verticalMove[y])



