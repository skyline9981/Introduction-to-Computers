from karel.stanfordkarel import *


def main():
    turn_right()
    while front_is_clear():
        safe_move()
        put_beeper()
    go_back()
    fill()


def fill():
    while front_is_clear():
        safe_move()
        turn_right()
        safe_move()
        while front_is_clear():
            safe_move()
            put_beeper()
        go_back()


def go_back():
    if not front_is_clear():
        turn_around()
        while on_beeper():
            move()
        turn_right()


def safe_move():
    if front_is_clear():
        move()


def turn_around():
    turn_left()
    turn_left()


def turn_right():
    for i in range(3):
        turn_left()


####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
