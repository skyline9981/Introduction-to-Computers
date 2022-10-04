from campy.graphics.gobjects import GOval
from campy.gui.events.timer import pause
from campy.graphics.gwindow import GWindow

VX=2
SIZE=10
window = GWindow(800,400)
DELAY=10
REDUCE=0.9
G=1
ball = GOval(SIZE,SIZE)


def main():
    ball.filled = True
    window.add(ball, 40, 30)
    v0 = 0
    vx = VX

    while True:
        bounce=True
        vy = v0 + G
        if ball.y + SIZE//2 >= window.height-5:
            bounce = False
        if bounce is False:
            vy = v0 * -REDUCE
        ball.move(vx, vy)
        v0 = vy
        if ball.x-SIZE//2 >= window.width:
            break
        pause(20)


if __name__ == '__main__':
    main()