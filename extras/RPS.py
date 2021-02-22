# Sebastian G. Maldonado Rosado
# Friday, December 6th, 2019
# CIIC 3011-086 Optional Project

"""Rock, Paper, Scissors
    The game!"""

import random

print('Welcome to Rock, Paper, Scissors the game!\nThe best of 5 wins')

# Plays that the user can make
valid_choices = ['rock', 'paper', 'scissors']

# Counters for the loop and scores
userCount = 0
cpuCount = 0
rounds = 0
roundDisplay = 0

# Runs 5 rounds of the game (tied rounds are not counted) or stops when either the cpu or user reaches a score of 3
while rounds < 5 and (userCount < 3 and cpuCount < 3):
    while True:  # Loop that keeps running until user makes a valid choice
        user_choice = input('\n--------------------------------------------------- \
        \nPlease choose and option (rock, paper or scissors): \n')  # Asks the user for their play
        if user_choice in valid_choices:  # Tests if the user's choice is a valid play
            break
        else:  # Runs when the user makes a wrong input
            print('---------------------------------------------------\nThat\'s not a valid choice! Try again')

    cpu_choice = random.choice(valid_choices)  # Chooses the computer's play
    if user_choice != cpu_choice:  # Shows the number of the played round; doesn't display for tied rounds
        print('(Round', roundDisplay+1, 'of 5)')
    print('\nYour choice is', user_choice)
    print('My choice is', cpu_choice + '\n')

    if (cpu_choice == 'rock' and user_choice == 'paper') or (cpu_choice == 'paper' and user_choice == 'scissors') \
            or (cpu_choice == 'scissors' and user_choice == 'rock'):  # Checks if the user won the round; CPU lost
        print(user_choice, 'beats', cpu_choice
              + '!\nYou win this round! :(\n---------------------------------------------------')
        userCount += 1  # Adds a won round to the user
        rounds += 1  # Indicates a round has been completed
        roundDisplay += 1

    elif (cpu_choice == 'paper' and user_choice == 'rock') or (cpu_choice == 'scissors' and user_choice == 'paper') \
            or (cpu_choice == 'rock' and user_choice == 'scissors'):  # Checks if the CPU won; user lost
        print(cpu_choice, 'beats', user_choice
              + '!\nYou lose, I win this round!\n---------------------------------------------------')
        cpuCount += 1  # Adds a won round to the CPU
        rounds += 1  # Indicates a round has been completed
        roundDisplay += 1

    elif cpu_choice == user_choice:  # If the user and CPU make the same play, none get points and round is not counted
        print('It\'s a tie!\n(This round will not be counted)\n---------------------------------------------------')

    print('(Your score: ' + str(userCount) + ' // ' + 'CPU score: ' + str(cpuCount) + ')')  # Displays the scores

# Displays the winner and the score
if userCount > cpuCount:
    print('\n---------------------------------------------------\nCongratulations, you win!',
          '(' + str(userCount) + ' to ' + str(cpuCount) + ')\n---------------------------------------------------')
else:
    print('\n---------------------------------------------------\nToo bad, you lose!',
          '(' + str(cpuCount) + ' to ' + str(userCount) + ')\n---------------------------------------------------')
