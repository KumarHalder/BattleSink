class player:
    #init
    def __init__(self,name, health=3):
        self.name = name
        self.opponentBoard =  [[0 for i in range(8)] for j in range(8)]
        self.opponentShipCoordinates = []
        self.opponentHealth = health

    #Place ship for opponent player
    def placeShip(self,x:int,y:int,isHorizontal:bool):
        if type(x) is not int or type(y) is not int or type(isHorizontal) is not bool:
            #print("invalid position, (x,y) values must be int, and isHorizontal should be boolean")
            return False
        #ship placed horizontally
        if isHorizontal:
            #Out of board
            if x > 6 or x < 1:
                return False
            if y > 7 or y < 0:
                return False
            #Set ship position
            for i in range(-1,2):
                self.opponentShipCoordinates.append([x+i,y])
        #ship placed vertically
        else:
            if x > 7 or x < 0:
                return False
            if y > 6 or y < 1:
                return False
            for i in range(-1,2):
                self.opponentShipCoordinates.append([x,y+i])
        #print(self.opponentShipCoordinates)
        return True

    #checks if the opponent ship is at fired position
    def isOpponentShipAtPosition(self,x,y):
        for coordinate in self.opponentShipCoordinates:
            if coordinate[0] == x and coordinate[1] == y :
                return True
        return False

    #checks if the move has been used previously by the player
    def isThisMoveUSedPreviously(self,x,y):
        if (self.opponentBoard[y][x] != 0 ):
            return True
        return False

    #shots at point (x,y)
    def shotPoint(self,x,y):
        #miss
        if self.isOpponentShipAtPosition(x,y) == False:
            print("miss")
            self.opponentBoard[y][x] = "X"
        #Hit
        else:
            print("hit")
            self.opponentBoard[y][x] = "hit"
            self.opponentBeenShot()
        #display board after each guess
        for x in self.opponentBoard:
            print(x)

    #Action when opponent ship is been shot
    def opponentBeenShot(self):
        self.opponentHealth -= 1
        #print("health: ", self.opponentHealth)

    #Action when opponent ship is destroyed
    def opponentDestroyed(self):
        if (self.opponentHealth <= 0):
            print("\n\n")
            print("...... ",self.name + " have won......")
            return True
        return False



