class board:
    def __init__(self,health=3):
        self.ownShip = [[0 for i in range(8)] for j in range(8)]
        self.opponentShip =  [[0 for i in range(8)] for j in range(8)]
        self.opponentBoard =  [[0 for i in range(8)] for j in range(8)]
        self.health = health

    def placeShip(self,x:int,y:int,isHorizontal:bool):
        if type(x) is not int or type(y) is not int or type(isHorizontal) is not bool:
            print("invalid position, (x,y) values must be int, and isHorizontal should be boolean")
            return
        #ship placed horizontally
        if isHorizontal:
            if x > 6 or x < 1:
                print("invalid position")
                return
            if y > 7 or y < 0:
                print("invalid position")
                return
            for i in range(-1,2):
                self.ownShip[y][x+i]='z'
        #ship placed vertically
        else:
            if x > 7 or x < 0:
                print("invalid position")
                return
            if y > 6 or y < 1:
                print("invalid position")
                return
            for i in range(-1,2):
                self.ownShip[y+i][x]='z'

    def shotPoint(self,x,y):
        # if (self.opponentBoard[y][x] != 0):
        #     return "try again"
        self.opponentBoard[y][x] = 1
        print(self.opponentBoard)
    def beenShot(self):
        self.health -=1
        print(self.health)

