# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math


# helper function to start and restart the game
def new_game(new_max):
    # initialize global variables used in your code here
    global minimum
    global maximum
    global guess
    global secret_number
    global secret_number_secret
    global guess_count
    global max_guess_count
    global show_secret
    minimum = 0
    maximum = new_max
    str_maximum = str(maximum)
    guess = 0
    secret_number = random.randrange(minimum, maximum)
    secret_number_secret = "psst... The secret number is %i" % secret_number
    guess_count = 0
    if maximum == 100:
        max_guess_count = 7
    else:
        max_guess_count = 10
    show_secret = False
    print '\nstarting new game\nrange is [0-' + str_maximum + ')\n'
    

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game(100)
    
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    new_game(1000)
    

def show_secret():
    global show_secret
    global secret_number_secret
    if show_secret == False:
        show_secret = True
        print secret_number_secret
    else:
        show_secret = False
        print "you can't see my secrets!"


def check_hilow(high, low):
    # check hilow, returns end_game status
    global secret_number
    global secret_number_secret
    if high == True:
        print "wrong. guess lower"
        if show_secret:
            print secret_number_secret
        return False
    elif low == True:
        print "wrong. guess higher"
        if show_secret:
            print secret_number_secret
        return False
    else:
        print "You got it!! Great Job!"
        return True

    
def check_turns(guess_count):
    # checks number of turns, returns endgame status
    global max_guess_count
    max_guess_string = "\nmax guesses @ %i reached.  Starting new game." % maximum
    if guess_count == max_guess_count:
        print max_guess_string
        return True
    else:
        return False
         
        
def input_guess(guess, guess_count):
    # main game logic goes here	
    global minimum
    global maximum
    global secret_number
    global max_guess_count
    high = guess > secret_number
    low = guess < secret_number
    max_guess_str = str(max_guess_count)        
    print "\nguess #", guess_count, "of " + max_guess_str + " is:", guess
    
    # check guess against secret_number
    # check_hilow() prints guess  right/wrong/how
    end_game = check_hilow(high, low)
    if end_game != True:
        # if guess != secret number, check # of turns
        end_game = check_turns(guess_count)
    if end_game == True:
        print '\n\n'
        new_game(maximum)

        
def enter(x):
    global guess
    global guess_count
    guess = int(x)
    guess_count += 1
    input_guess(guess, guess_count)
    
    
# create frame
gn = simplegui.create_frame("Guess the Number",300,300)

# register event handlers for control elements and start frame
gn.add_button("Range is [0,100)",range100,100)
gn.add_button("Range is [0,1000)",range1000,100)
gn.add_button("Show Secret on/off",show_secret,100)
gn.add_input("Enter Guess", enter, 100)
gn.start()
# call new_game 
new_game(100)


# always remember to check your completed program against the grading rubric
