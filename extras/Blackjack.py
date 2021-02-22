# Sebastian G. Maldonado Rosado
# Thursday, December 12th, 2019
# CIIC 3011-086 Optional Project

"""Blackjack (simplified)"""

import random


def deal():
    """Returns a random number between 1 and 11."""
    return random.randint(1, 11)


def deal_two():
    """Returns a number that is the sum of two numbers between 1 and 11."""
    one = deal()
    two = deal()
    result = one + two
    if result == 22:  # If the two starting cards are more than 21, reduce the score to 12.
        return 12
    else:  # Otherwise, get original score.
        return result


def is_blackjack(num):
    """Return True if a given number is exactly 21 (Blackjack!), or False otherwise."""
    if num == 21:
        return True
    else:
        return False


def is_bust(num):
    """Returns true if a given number is more than 21 (a bust!), or False otherwise."""
    if num > 21:
        return True
    else:
        return False


def should_hit(num):
    """Return true if a given number is 16 or less (dealer always hits if the total is less than 17),
    or False otherwise."""
    if num <= 16:
        return True
    else:
        return False


def play_dealer():
    """Deals two cards for the dealer and returns their value."""
    dealer_cards = deal_two()  # Deals the starting cards to the dealer.
    print('The dealer has a score of ' + str(dealer_cards) + '.')
    while should_hit(dealer_cards) is True:  # If the dealer has a score lower than 17, then it hits again.
        new_card = deal()
        dealer_cards += new_card
        print('The dealer chooses to hit, and draws a ' + str(new_card) + '.')
        if should_hit(dealer_cards) is False:
            print('The dealer stops with a ' + str(dealer_cards) + '.\n')
            return dealer_cards
    else:  # Otherwise, it gets their final score.
        print('The dealer stops with a ' + str(dealer_cards) + '.\n')
        return dealer_cards


def play_player():
    """Deals two card for the player, and keeps asking of the player would like to hit until they bust or input no, and
    returns their value."""
    valid_y = ['y', 'Y', 'yes', 'Yes']  # Indicates valid 'yes' choices.
    valid_n = ['n', 'N', 'no', 'No']  # Indicates valid 'no' choices.
    player_cards = deal_two()  # Deals the starting cards to the player.
    print('You have a score of ' + str(player_cards) + '.')
    while True:
        choice = input('Do you want to draw another card? (Y/N)\n')
        if choice in valid_y:  # Deals a new card if player says 'yes'.
            new_card = deal()
            print('You hit and draw a ' + str(new_card) + '.')
            player_cards += new_card
            if is_bust(player_cards):  # Stops if player busts while getting the new card.
                print('You stop with a ' + str(player_cards) + '.\n')
                return player_cards
            else:  # If player doesn't bust, keep asking if they wish to deal again.
                print('Your score is ' + str(player_cards) + '.')
                continue
        elif choice in valid_n:  # Player decides 'no', and gets their final score.
            print('You stop with a ' + str(player_cards) + '.\n')
            return player_cards
        else:  # If a wrong input was received, try again.
            print('That\'s not a valid choice, try again!')


def play_game(money):
    """Plays the game with its different rules."""
    money = float(money)
    print('\nYou bet $' + str(money) + '.')
    player_score = play_player()  # Determines the player's cards and score
    dealer_score = play_dealer()  # Determines the dealer's cards and score
    if is_bust(player_score) is False and is_bust(dealer_score) is True:  # When the dealer loses.
        if player_score == 21:  # Player gets triple the money if they hit a Blackjack.
            money = money * 3
            print('Blackjack! You win $' + str(money) + ' dollars.')
            return money
        else:  # Double the money otherwise.
            money = money * 2
            print('You win! You won $' + str(money) + ' dollars.')
            return money
    elif (is_bust(dealer_score) is True and is_bust(player_score) is True) or \
            ((is_bust(dealer_score) is False and is_bust(player_score) is False) and player_score == dealer_score):
        # If both the player and dealer bust or they tie, the game "pushes" and the player gets their money back.
        print('The game is a push. You win $' + str(money) + ' dollars.')
        return money
    elif is_bust(dealer_score) is False and is_bust(player_score) is False:  # If none bust.
        if player_score == 21 and dealer_score != 21:  # If the PLayer hits a Blackjack, they get triple the money.
            money = money * 3
            print('Blackjack! You win $' + str(money) + ' dollars.')
            return money
        elif player_score > dealer_score:  # If the dealer has a lower score than the player, player gets double money.
            money = money * 2
            print('You win! You won $' + str(money) + ' dollars.')
            return money
        else:  # Otherwise, the dealer wins and player loses money.
            print('You lose! The dealer wins.\nYou won $0.0 dollars.')
            return 0.0
    else:  # If no previous conditions were met, assume dealer wins and player gets no money.
        print('You lose! The dealer wins.\nYou won $0.0 dollars.')
        return 0.0


def ask():  # Destructive function
    """Asks the user if they would like to play again."""
    while True:
        ask = input('\nWould You like to play again? (Y/N)\n')
        if ask in valid_y:
            return True
        elif ask in valid_n:
            print('Thanks for playing!')
            return False
        else:  # Check this later
            print('That\'s not a valid input, try again!')
            continue


while True:
    valid_y = ['y', 'Y', 'yes', 'Yes']  # Indicates valid 'yes' choices.
    valid_n = ['n', 'N', 'no', 'No']  # Indicates valid 'no' choices.

    while True:
        money = input('How many dollars would you like to bet?\nEnter: $')
        try:
            money = float(money)
            break
        except:
            print('That\'s not a valid amount, try again!')
            continue

    play_game(money)
    question = ask()

    if question is False:
        break
