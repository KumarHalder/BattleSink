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


    def placePlayerShip(self,player:player):
        x, y, isHorizontal = input(str(player.name)+" ship position: x:int,  y:int , H/V: str : ").split()
        while (player.placeShip(self.horizontalMove[x], self.verticalMove[y], isHorizontal == "H") == False):
            x, y, isHorizontal = input(str(player.name)+" ship position: x:int,  y:int , H/V: str : ").split()



    def setPlayerTurn(self):
        print("turnCount: ", self.turn)
        if self.turn % 2 == 0:
            self.turn += 1
            self.player1turn = True
            return "Player1 turn: "
        self.turn += 1
        self.player1turn = False
        return "Player2 turn: "

    def firedAtPosition(self,x,y):
        if self.player1turn:
            self.player1.shotPoint(x, y)
        else:
            self.player2.shotPoint(x, y)

    def isThisMoveUSedPreviously(self,x,y):
        if self.player1turn:
            return self.player1.isThisMoveUSedPreviously(x, y)
        else:
            return self.player2.isThisMoveUSedPreviously(x, y)

    def isValidMove(self,x,y):
        if (x > 7 or x < 0 or y > 7 or y < 0):
            return False
        elif self.isThisMoveUSedPreviously(x, y):
            return False
        return True

    def isGameOver(self):
        if (self.player1.opponentDestroyed() or self.player2.opponentDestroyed()) == True:
            print("..........Game Over..........")
            return True
        return False

    def gameStart(self):
        while (self.isGameOver() == False):
            print(self.setPlayerTurn())
            x, y = input("fire at position x y : ").split()
            # x,y = int(x),int(y)
            if self.isValidMove(self.horizontalMove[x], self.verticalMove[y]):
                self.firedAtPosition(self.horizontalMove[x], self.verticalMove[y])
            else:
                while self.isValidMove(self.horizontalMove[x], self.verticalMove[y]) == False:
                    print(
                        "Invalid Move, please try again, possible cause - out of board position/previously same used position")
                    x, y = input("fire at position x y : ").split()
                    # x, y = int(x), int(y)
                self.firedAtPosition(self.horizontalMove[x], self.verticalMove[y])

game = gameManager()
game.placePlayerShip(game.player1)
game.placePlayerShip(game.player2)
game.gameStart()



