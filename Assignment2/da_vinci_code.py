"""
File: da_vinci_code.py
ID:0711506
author:WEI-CHENG, Wang
-----------------------
This program should implement a console program
that plays a game of guessing a number determined by
the game designer (that is the constant SECRET at the top).
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

SECRET = 63
UPPER_BOUND = 99
LOWER_BOUND = 0
# You can change the value of SECRET, UPPER_BOUND, and LOWER_BOUND here.


def main():
    """
    This is a game for guessing a number called SECRET.
    If you guess a number higher than the SECRET, it
    will show you 'The number you guess was higher than the secret number.'
    If you guess lower, it will show 'The number you guess was lower than the secret number.'
    """
    pass
    guess()
    input_number = int(input())
    while not input_number == SECRET:
        if UPPER_BOUND >= input_number > SECRET:
            print('You guess ', input_number, ' was higher than the secret number')
            if input_number - SECRET <= 5:
                separation_line()
                print('It is very close!!')
                print('٩(๑•̀ω•́๑)۶')
            # If your number is higher or lower than SECRET in 5 numbers, it will tell you are close.
            separation_line()
            guess()
        elif LOWER_BOUND <= input_number < SECRET:
            print('You guess ', input_number, ' was lower than the secret number')
            if SECRET - input_number <= 5:
                separation_line()
                print('It is very close!!')
                print('٩(๑•̀ω•́๑)۶')
            # If your number is higher or lower than SECRET in 5 numbers, it will tell you are close.
            separation_line()
            guess()
        elif LOWER_BOUND > input_number:
            print('Error!!!')
            print('┴─┴︵╰（‵□′╰）')
        # When you input a number out of the range(LOWER_BOUND~UPPER_BOUND), it will show 'Error!'
            separation_line()
            guess()
        elif input_number > UPPER_BOUND:
            print('Error!!!')
            print('(╯‵□′)╯︵┴─┴')
        # When you input a number out of the range(LOWER_BOUND~UPPER_BOUND), it will show 'Error!'
            separation_line()
            guess()
        input_number = int(input())
    if input_number == SECRET:
        print('Congrats! The secret number was: ', SECRET)
        print('｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡')

def separation_line():
    """
    Use '=' to print a separation line.
    """
    for i in range(21):
        print('=', end='')
    print('')

def guess():
    """
    Ask you to guess a number.
    """
    print('Guess a number from ', LOWER_BOUND, ' to', UPPER_BOUND, ':', end='')

###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == '__main__':
    main()
