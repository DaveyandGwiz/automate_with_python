import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in your code.

        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        #  'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #            ('green', 'shotgun')]}

        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break


# A bot that stops rolling after it has rolled two shotguns
class Stop2ShotgunsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        shotguns = 0
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            shotguns += diceRollResults['shotgun']
            if shotguns < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
# A bot that, after the first roll, randomly decides if it will continue or stop
class RandomZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        shotguns = 0
        diceRollResults = zombiedice.roll() # first roll

        while diceRollResults is not None:
            random_integer = random.randint(1, 2)
            if random_integer == 1:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

# A bot that stops rolling after it has rolled two brains
class Stop2BrainsZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        brains = 0
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains >= 2:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again
# A bot that initially decides it’ll roll the dice one to four times, but will stop early if it rolls two shotguns
class StopAt4Rolls:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        rolls = random.randint(1, 4)
        numOfRolls = 0
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults is not None:
            numOfRolls += 1
            if numOfRolls < rolls and not diceRollResults['shotgun'] >= 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
# A bot that stops rolling after it has rolled more shotguns than brains
class StopIfShotgunsGtrBrains:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll
        while diceRollResults is not None:
            if diceRollResults['shotgun'] > diceRollResults['brains']:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 \
    Shotguns', minShotguns=2),\
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 \
    Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
    # Add any other zombie players here.
    Stop2ShotgunsZombie(name='Dave'),
    RandomZombie(name='Steve'),
    Stop2BrainsZombie(name='Arsene'),
    StopAt4Rolls(name='Bill Clinton'),
    StopIfShotgunsGtrBrains(name='Spock')

)

# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)