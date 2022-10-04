from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
ID:0711506
Author:Wei_Cheng Wang
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds supplied in the starter folder.
"""


def main():
    """
    Karel will draw a checkerboard by beepers.

    """
    put_first_row()
    if facing_east():
        while left_is_clear():
          put_one_row()
    if right_is_clear():
        put_one_row()


def go_to_next_row():
    """
    To make Karel go to the next row and face east.

    """
    turn_left()
    safe_move()
    turn_right()


def put_first_row():
    """
    To make Karel draw the first row.

    """
    put_beeper()
    while front_is_clear():
        safe_move()
        safe_move()
        put_beeper()
    turn_around()
    safe_move()
    if on_beeper():
        turn_around()
        safe_move()
        pick_beeper()
        turn_around()
        if not front_is_clear():
            put_beeper()
            turn_around()
        else:
            turn_around()
            safe_move()
    else:
        turn_around()
        safe_move()
    turn_around()
    while front_is_clear():
        safe_move()
    turn_around()
    go_to_next_row()


def put_one_row():
    """
    To make Karel draw others row.

    """
    if not front_is_clear():
        turn_right()
        safe_move()
        if not on_beeper():
            turn_around()
            safe_move()
            turn_right()
            put_beeper()
        else:
            turn_around()
            safe_move()
            turn_right()
    while front_is_clear():
        turn_right()
        safe_move()
        if not on_beeper():
            turn_around()
            safe_move()
            turn_right()
            put_beeper()
            safe_move()
        else:
            turn_around()
            safe_move()
            turn_right()
            safe_move()
            put_beeper()
            safe_move()
    turn_around()
    while front_is_clear():
        safe_move()
    turn_around()
    go_to_next_row()


def turn_around():
    """
    To make Karel turn_left 2 times.

    """
    turn_left()
    turn_left()


def turn_right():
    """
    To make Karel turn_left 3 times.

    """
    turn_left()
    turn_left()
    turn_left()


def safe_move():
    """
    To make Karel move safety.

    """
    if front_is_clear():
        move()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)