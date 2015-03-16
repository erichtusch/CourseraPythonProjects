__author__ = 'Erich Tusch'

# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    # pass

    name = name.upper()
    output_num = 0
    if name == 'ROCK':
        output_num = 0
    elif name == 'SPOCK':
        output_num = 1
    elif name == 'PAPER':
        output_num = 2
    elif name == 'LIZARD':
        output_num = 3
    elif name == 'SCISSORS':
        output_num = 4
    return output_num

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    # pass
    if number == 0:
        output_name = 'rock'
    elif number == 1:
        output_name = 'Spock'
    elif number == 2:
        output_name = 'paper'
    elif number == 3:
        output_name = 'lizard'
    elif number == 4:
        output_name = 'scissors'
    return output_name
    # convert number to a name using if/elif/else
    # don't forget to return the result!


def rpsls(player_choice):
    # delete the following pass statement and fill in your code below
    #pass

    # print a blank line to separate consecutive games
    print
    # print out the message for the player's choice
    print 'Player chooses ' + player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    # need to figure out how to use the below function
    comp_number = random.randrange(0, 5, 1)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    # compute difference of comp_number and player_number modulo five
    mod_score = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if mod_score == 1 or mod_score == 2:
        print "Computer wins!"
    elif mod_score == 3 or mod_score == 4:
        print 'Player wins!'
    else:
        print "Player and computer tie!"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

