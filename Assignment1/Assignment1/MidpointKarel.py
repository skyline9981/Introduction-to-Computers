from karel.stanfordkarel import *

"""
File: MidpointKarel.py
ID:0711506
Author:Wei_Cheng Wang
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Karel will find the midpoint of 1st Street.
    """
    move_to_wall()
    move_to_mid()
    put_beeper()


def move_to_wall():
    """
    To make Karel go to the edge of 1st Street.

    """
    while front_is_clear():
        move()
        put_beeper()


def move_to_mid():
    """
    To make Karel go back to the midpoint of 1st Street.

    """
    turn_around()
    if on_beeper():
        pick_beeper()
    safe_move()
    while on_beeper():
        while on_beeper():
            safe_move()
        turn_around()
        move()
        pick_beeper()
        safe_move()
    turn_around()
    safe_move()


def safe_move():
    """
    To make Karel move safety.

    """
    if front_is_clear():
        move()


def turn_around():
    """
    To make Karel turn_left 2 times.

    """
    turn_left()
    turn_left()



####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)