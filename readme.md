##BattleField

This is a console version offline game of battlefield in python 3. For the demo purpose, there isonly one ship of length 3 units. Following image visualises the scenario. 
####Set-up
This console game does not require any additional package, for testing pytest has been used. For playing, run game.py script. Run the following command in the downloaded repo. 
```buildoutcfg
python3 game.py
```
or depending on how your python is set up,
```buildoutcfg
python game.py
```

####GamePlay
.......RULES OF GAME.............<br />

Two player game, each player takes turn after another.
First turn is for placing ships by each player, it takes three arguments of space separated value,
      where first two are coordinates of the ship center, and the last is H/V, providing the placement of the ship
      horizontally or vertically, as shown in the figure (example: A 2 H))
After placement, each player guesses and fires by coordinates in space separated values (example: B 5) <br />
.........Lets have fun ........

![Alt text](screenshots/diagram.png?raw=true "Game Play")


####Testing

The game is developed in Test Driven Deployment. Python module pytest is used for testing script test_game.py. For installing pytest,

1. Run the following command in your command line:
2. Check that you installed the correct version:

```bash
pip install -U pytest
```

```bash
$ pytest --version
This is pytest version 5.x.y, imported from $PYTHON_PREFIX/lib/python3.5/site-packages/pytest/__init__.py

```
After installation, test with 
```
$ pytest -q test_game.py
```

Test Result Sample:

![Alt text](screenshots/testResult.png?raw=true "Game Play")

  