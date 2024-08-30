import random

entry = random.randint(1, 2)

selections = ['ROCK', 'PAPER', 'SCISSORS']

print("select 0 for rock 1 for paper and 2 for scissors")
print('ROCK, PAPER, SCISSORS, shoot!')
ties, wins, losses = 0,0,0

playerMove = input()
computerMove = selections[entry]

# Display and record the win/loss/tie:
if playerMove == computerMove:
    print("I chose "+computerMove)
    print('It is a tie!')
    ties = ties + 1
elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
    print("I chose "+computerMove)
    print('You win!')
    wins = wins + 1
elif playerMove == 'PAPER' and computerMove == 'ROCK':
    print("I chose "+computerMove)
    print('You win!')
    wins = wins + 1
elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
    print("I chose "+computerMove)
    print('You win!')
    wins = wins + 1
elif playerMove == 'ROCK' and computerMove == 'PAPER':
    print("I chose "+computerMove)
    print('You lose!')
    losses = losses + 1
elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
    print("I chose "+computerMove)
    print('You lose!')
    losses = losses + 1
elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
    print("I chose "+computerMove)
    print('You lose!')
    losses = losses + 1

print("game over")