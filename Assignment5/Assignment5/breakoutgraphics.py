"""
ID:0711506
AUTHOR:王偉誠
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 750      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).
INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle.
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.paddle.fill_color = "black"
        self.window.add(self.paddle, x=window_width // 2 - paddle_width // 2, y=window_height - paddle_offset)
        # Center a filled ball in the graphical window.
        self.ball = GOval(width=2*ball_radius, height=2*ball_radius)
        self.ball.filled = True
        self.ball.fill_color = "black"
        self.window.add(self.ball, x=(self.window.width - self.ball.width) // 2,
                        y=(self.window.height - self.ball.height) // 2)
        # Default initial velocity for the ball.
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.uniform(0, 1) > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
        # Draw bricks.
        for row in range(brick_rows):
            color = ["red", "orange", "yellow", "green", "blue"]
            for column in range(brick_cols):
                brick = GRect(width=brick_width, height=brick_height)
                brick.filled = True
                brick.fill_color = color[row // 2]
                self.window.add(brick, x=column * (brick_width + brick_spacing),
                                y=row * (brick_height + brick_spacing) + brick_offset)
        # calculate the number of bricks.
        self.brick = brick_rows * brick_cols
        # Initialize our mouse listeners.
        self.start = False
        onmouseclicked(self.play)
        onmousemoved(self.move_paddle)

    # the getter of self.__dx
    def get_vx(self):
        return self.__dx

    # the getter of self.__dy
    def get_vy(self):
        return self.__dy

    # if you click the mouse once, it will start the game.
    def play(self, event):
        self.start = True

    # you can change the position of the paddle with your mouse.
    def move_paddle(self, event):
        if 0 <= event.x - PADDLE_WIDTH // 2 and event.x + PADDLE_WIDTH // 2 <= self.window.width:
            self.paddle.x = event.x - PADDLE_WIDTH//2

    # if you miss the ball, it will reset the position of the ball.
    def reset_ball(self):
        self.window.add(self.ball, x=(self.window.width - self.ball.width) // 2,
                        y=(self.window.height - self.ball.height) // 2)
        self.start = False
