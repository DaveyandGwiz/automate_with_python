

# Write a program to find out how often a streak of six heads or a streak of six tails comes up
# in a randomly generated list of heads and tails.
# Your program breaks up the experiment into two parts:

# the first part generates a list of randomly selected 'heads' and 'tails' values,

# and the second part checks if there is a streak in it.

# Put all of this code in a loop that repeats the experiment 10,000 times
# so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row.
# As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time
# and a 1 value the other 50% of the time.



import random
numberOfStreaks = 0
# one thousand times I will flip a cone 100 times and see if I get 6 heads or tails in a row
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    listHT = ''
    # flip a coin 100 times
    for i in range(100):
        randomNumber = random.choice([1, 2])
        if randomNumber == 1:
            listHT = listHT + 'H'
        else:
            listHT = listHT + 'T'
    # Code that checks if there is a streak of 6 heads or tails in a row.
    if 'HHHHHH'in listHT or 'TTTTTT' in listHT:
        numberOfStreaks = numberOfStreaks + 1

# numberOfStreaks is the number of times I got six in a row of 100 flips
# The empirical probability of getting six heads or tails in a row when you flip 100 times is
# equal to numberOfStreaks / 10,000
# this probability in percent is (numberOfStreaks/10,000)*100%
probabilityOfStreak = (numberOfStreaks / 10000) * 100
print('Chance of streak: %s%%' % probabilityOfStreak)









