from player import player

class gameManager:
    #init
    def __init__(self):
        self.player1 = player("player1")
        self.player2 = player("player2")
        self.turn = 0
        self.player1turn = True
        self.horizontalMove = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
        self.verticalMove = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7}

    #ship placement per player. (x,y) are midpoint coordinates of ship, H/V is horizontal/vertical placement,
    def placePlayerShip(self,player:player):
        x, y, isHorizontal = input(str(player.name)+" ship position: x:[A-H],  y:[1-8] , H/V: str : ").split()
        while (x not in self.horizontalMove or y not in self.verticalMove or isHorizontal not in ['H','V'] or  player.placeShip(self.horizontalMove[x], self.verticalMove[y], isHorizontal == "H") == False):
            print("Invalid Position, try again")
            x, y, isHorizontal = input(str(player.name)+" ship position:  x:[A-H],  y:[1-8] , H/V: str : ").split()

    #change turn function after each move
    def setPlayerTurn(self):
        print("turnCount: ", self.turn)
        if self.turn % 2 == 0:
            self.turn += 1
            self.player1turn = True
            return "Player1 turn: "
        self.turn += 1
        self.player1turn = False
        return "Player2 turn: "

    #Fire function for players
    def firedAtPosition(self,x,y):
        x = self.horizontalMove[x]
        y = self.verticalMove[y]
        if self.player1turn:
            self.player1.shotPoint(x, y)
        else:
            self.player2.shotPoint(x, y)

    #checks if the same move was done previously
    def isThisMoveUSedPreviously(self,x,y):
        if self.player1turn:
            return self.player1.isThisMoveUSedPreviously(x, y)
        else:
            return self.player2.isThisMoveUSedPreviously(x, y)

    #Checks if the user input is valid for movement
    def isValidMove(self,x,y):
        if x not in self.horizontalMove or y not in self.verticalMove:
            return False
        x = self.horizontalMove[x]
        y = self.verticalMove[y]
        if (x > 7 or x < 0 or y > 7 or y < 0):
            return False
        elif self.isThisMoveUSedPreviously(x, y):
            return False
        return True

    #game over
    def isGameOver(self):
        if (self.player1.opponentDestroyed() or self.player2.opponentDestroyed()) == True:
            print("..........Game Over..........")
            return True
        return False

    #starts game and continues untill gameover
    def gameStart(self):
        while (self.isGameOver() == False):
            print(self.setPlayerTurn())
            x, y = input("fire at position x y : ").split()
            if  self.isValidMove(x,y):
                self.firedAtPosition(x,y)
            else:
                while self.isValidMove(x,y) == False:
                    print(
                        "Invalid Move, please try again, possible cause - out of board position/previously same used position/Invalid Input")
                    x, y = input("fire at position x y : ").split()
                self.firedAtPosition(x,y)




