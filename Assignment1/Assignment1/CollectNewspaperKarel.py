from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
ID:0711506
Author:Wei_Cheng Wang
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Karel will go out to pick a newspaper and go home.
    """
    get_newspaper()
    go_home()


def get_newspaper():
    """
    To make Karel get the newspaper.

    """
    while front_is_clear():
        move()
    turn_right()
    while not left_is_clear():
        move()
    turn_left()
    while not on_beeper():
        move()
    if on_beeper():
        pick_beeper()
        turn_around()


def turn_around():
    """
    To make Karel turn left twice.
    """
    for i in range(2):
        turn_left()


def turn_right():
    """
    To make Karel turn left three times.
    """
    for i in range(3):
        turn_left()


def go_home():
    """
    When Karel gets newspaper, let karel go home.
    """
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    put_beeper()
    turn_right()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
