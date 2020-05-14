from gameManager import gameManager

print(".......RULES OF GAME.............")
print("two player game, each player takes turn after another")
print("first turn is for placing ships by each player, it takes three arguments of space separated value,\n"
      "where first two are coordinates of the ship center, and the last is H/V, providing the placement of \nthe ship"
      "horizontally or vertically (example: A 2 H)")
print("after placement, each player guesses and fires by coordinates in space separated values (example: C 2)")
print(".........Lets have fun ........\n\n\n")


game = gameManager()
game.placePlayerShip(game.player1)
game.placePlayerShip(game.player2)
game.gameStart()