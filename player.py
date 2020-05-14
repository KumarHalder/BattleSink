class player:
    def __init__(self,name, health=3):
        #self.ownShip = [[0 for i in range(8)] for j in range(8)]
        self.name = name
        self.opponentBoard =  [[0 for i in range(8)] for j in range(8)]
        self.opponentShipCoordinates = []
        self.opponentHealth = health

    def placeShip(self,x:int,y:int,isHorizontal:bool):
        if type(x) is not int or type(y) is not int or type(isHorizontal) is not bool:
            print("invalid position, (x,y) values must be int, and isHorizontal should be boolean")
            return False
        #ship placed horizontally
        if isHorizontal:
            #Out of board
            if x > 6 or x < 1:
                print("invalid position")
                return False
            if y > 7 or y < 0:
                print("invalid position")
                return False
            #Set ship position
            for i in range(-1,2):
                self.opponentShipCoordinates.append([x+i,y])
        #ship placed vertically
        else:
            if x > 7 or x < 0:
                print("invalid position")
                return False
            if y > 6 or y < 1:
                print("invalid position")
                return False
            for i in range(-1,2):
                self.opponentShipCoordinates.append([x, y+i ])
        print(self.opponentShipCoordinates)
        return True

    def isOpponentShipAtPosition(self,x,y):
        for coordinate in self.opponentShipCoordinates:
            if coordinate[0] == x and coordinate[1] == y :
                return True
        return False
    def isThisMoveUSedPreviously(self,x,y):
        if (self.opponentBoard[y][x] != 0 ):
            return True
        return False

    def shotPoint(self,x,y):
        #check if move is invalid

        #miss
        if self.isOpponentShipAtPosition(x,y) == False:
            print("miss")
            self.opponentBoard[y][x] = "X"

        #Hit
        else:
            print("hit")
            self.opponentBoard[y][x] = "hit"
            self.opponentBeenShot()


        for x in self.opponentBoard:
            print(x)


    def opponentBeenShot(self):
        self.opponentHealth -= 1
        #print("health: ", self.opponentHealth)


    def opponentDestroyed(self):
        if (self.opponentHealth <= 0):
            print("...... ",self.name + " have won......")
            return True
        return False



