"""
ID:0711506
AUTHOR:王偉誠
"""
from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel
from breakoutgraphics1 import BreakoutGraphics
import random

FRAME_RATE = 1000 / 120  # 120 frames per second.
NUM_LIVES = 3  # how many times you can miss the ball
graphics = BreakoutGraphics()
dx = graphics.get_vx()  # the speed of the ball
dy = graphics.get_vy()  # the speed of the ball
Y_SPEED = -7.0  # the speed of the ball
score = 0  # calculate the score.
# make the score_board.
score_board = GLabel("Score: " + str(score), 0, graphics.window.height)
graphics.window.add(score_board)


def main():
    """
    this program will make a funny game.
    you can move the paddle to keep the ball move and break the bricks.
    the score_board will record you scores.
    if you want to end the game, just click the "end game".
    """
    life = NUM_LIVES  # how many times you can miss the ball
    # Add animation loop here!
    while True:
        if graphics.start is True and life != 0 and graphics.brick != 0:
            global dx, dy
            graphics.ball.move(dx, dy)
            maybe_x = graphics.ball.x
            maybe_y = graphics.ball.y
            maybe_x1 = graphics.ball.x + graphics.ball.width
            maybe_y1 = graphics.ball.y + graphics.ball.height
            if bounce_brick(maybe_x, maybe_y, maybe_x, maybe_y1, maybe_x1, maybe_y, maybe_x1, maybe_y1):
                remove(maybe_x, maybe_y, maybe_x, maybe_y1, maybe_x1, maybe_y, maybe_x1, maybe_y1)
                global score
                score += 1
                score_board.text = "Scores: " + str(score)  # update the score.
                dy = -1 * dy  # change the direction of the ball.
            elif bounce_paddle(maybe_x, maybe_y, maybe_x, maybe_y1, maybe_x1, maybe_y, maybe_x1, maybe_y1):
                dy = Y_SPEED  # change the direction of the ball.
            elif bounce_up(maybe_y):
                dy = -1 * dy  # change the direction of the ball.
            elif bounce_l(maybe_x):
                dx = -dx  # change the direction of the ball.
            elif bounce_r(maybe_x1):
                dx = -dx  # change the direction of the ball.
            if scare(maybe_x, maybe_y, maybe_x, maybe_y1, maybe_x1, maybe_y, maybe_x1, maybe_y1):
                graphics.window.add(graphics.scareimg)
                pause(1000)
                graphics.window.remove(graphics.scareimg)
            if maybe_y1 >= graphics.paddle.y + graphics.paddle.height * 2:
                graphics.reset_ball()  # if you miss the ball, it will reset the position of the ball.
                life -= 1  # if you miss the ball, you will lose a life.
            if graphics.brick == 0:
                graphics.window.add(graphics.win)  # if you have break all of the bricks, you win.
                break
        elif life == 0:
            # if you have lost all lives, you lose.
            graphics.window.add(graphics.lose, x=0, y=graphics.window.height//4)
            break
        pause(FRAME_RATE)


def bounce_l(x):
    """
    check whether the ball reaches the left boundary or not.
    """
    if x < 0:
        return True


def bounce_r(x1):
    """
    check whether the ball reaches the right boundary or not.
    """
    if x1 > graphics.window.width:
        return True


def bounce_up(y):
    """
    check whether the ball reaches the upper boundary or not.
    """
    if y < 0:
        return True


def scare(x, y, x1, y1, x2, y2, x3, y3):
    obj = graphics.window.get_object_at(x, y)
    obj1 = graphics.window.get_object_at(x1, y1)
    obj2 = graphics.window.get_object_at(x2, y2)
    obj3 = graphics.window.get_object_at(x3, y3)
    if obj == graphics.scare:
        return True
    elif obj1 == graphics.scare:
        return True
    elif obj2 == graphics.scare:
        return True
    elif obj3 == graphics.scare:
        return True


def bounce_paddle(x, y, x1, y1, x2, y2, x3, y3):
    """
    check whether the ball reaches the paddle or not.
    """
    obj = graphics.window.get_object_at(x, y)
    obj1 = graphics.window.get_object_at(x1, y1)
    obj2 = graphics.window.get_object_at(x2, y2)
    obj3 = graphics.window.get_object_at(x3, y3)
    if obj == graphics.paddle:
        return True
    elif obj1 == graphics.paddle:
        return True
    elif obj2 == graphics.paddle:
        return True
    elif obj3 == graphics.paddle:
        return True


def bounce_brick(x, y, x1, y1, x2, y2, x3, y3):
    """
    check whether the ball reaches the bricks or not.
    """
    obj = graphics.window.get_object_at(x, y)
    obj1 = graphics.window.get_object_at(x1, y1)
    obj2 = graphics.window.get_object_at(x2, y2)
    obj3 = graphics.window.get_object_at(x3, y3)
    if obj is not None and obj != graphics.paddle and obj != score_board and obj != graphics.end\
            and obj != graphics.scare:
        return True
    elif obj1 is not None and obj1 != graphics.paddle and obj1 != score_board and obj1 != graphics.end\
            and obj1 != graphics.scare:
        return True
    elif obj2 is not None and obj2 != graphics.paddle and obj2 != score_board and obj2 != graphics.end\
            and obj2 != graphics.scare:
        return True
    elif obj3 is not None and obj3 != graphics.paddle and obj3 != score_board and obj3 != graphics.end\
            and obj3 != graphics.scare:
        return True


def remove(x, y, x1, y1, x2, y2, x3, y3):
    """
    remove the brick which is reached by the ball.
    """
    obj = graphics.window.get_object_at(x, y)
    obj1 = graphics.window.get_object_at(x1, y1)
    obj2 = graphics.window.get_object_at(x2, y2)
    obj3 = graphics.window.get_object_at(x3, y3)
    if obj is not None and obj != graphics.paddle and obj != score_board and obj != graphics.end\
            and obj != graphics.scare:
        graphics.window.remove(obj)
        graphics.brick -= 1
    elif obj1 is not None and obj1 != graphics.paddle and obj1 != score_board and obj1 != graphics.end\
            and obj1 != graphics.scare:
        graphics.window.remove(obj1)
        graphics.brick -= 1
    elif obj2 is not None and obj2 != graphics.paddle and obj2 != score_board and obj2 != graphics.end\
            and obj2 != graphics.scare:
        graphics.window.remove(obj2)
        graphics.brick -= 1
    elif obj3 is not None and obj3 != graphics.paddle and obj3 != score_board and obj3 != graphics.end\
            and obj3 != graphics.scare:
        graphics.window.remove(obj3)
        graphics.brick -= 1


if __name__ == '__main__':
    main()
