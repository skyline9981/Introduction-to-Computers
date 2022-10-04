from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
ID:0711506
Author:Wei_Cheng Wang
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    Karel will build columns for a building by beepers.

    """
    while front_is_clear():
        repair()
    if not front_is_clear():
        if not right_is_clear():
            turn_left()
            repair()


def repair():
    """
    Karel will repair the columns for different conditions.

    """
    if facing_east():
        turn_left()
    if not on_beeper():
        while not on_beeper():
            put_beeper()
            safe_move()
    else:
        jump_beeper()
    while not on_beeper():
        put_beeper()
        safe_move()
    else:
        jump_beeper()
    while not on_beeper():
        put_beeper()
        safe_move()
    else:
        jump_beeper()
    while not on_beeper():
        put_beeper()
        safe_move()
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_right()
        for i in range(4):
            safe_move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


def jump_beeper():
    """
    To make Karel keep away from beeper.

    """
    if on_beeper():
        safe_move()


def safe_move():
    """
    To make Karel move safety.

    """
    if front_is_clear():
        move()


def turn_right():
    """
    To make Karel turn_left 3 times.

    """
    for i in range(3):
        turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)