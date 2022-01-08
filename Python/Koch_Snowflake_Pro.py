import math
import turtle as t
from colorsys import hsv_to_rgb


def rad(tup: tuple):
    x, y = tup
    ra = math.atan2(y, x)
    return ra / math.pi / 2 * 0.5


def xh_fd(n, length):
    if n == 0:
        t.pencolor(hsv_to_rgb(rad(t.pos()), 1, 1))
        t.forward(length)
    else:
        xh_fd(n - 1, length / 3)
        t.right(60)


t.tracer(0, 0)
t.hideturtle()


def flake(a, n):
    h = 0.01
    if n == 0:
        t.forward(a)
        return
    flake(a / 3, n - 1)
    t.left(60)
    h += 0.01
    flake(a / 3, n - 1)
    t.right(120)
    h += 0.01
    flake(a / 3, n - 1)
    t.left(60)
    h += 0.01
    flake(a / 3, n - 1)


i = 500
j = 2

t.up()
t.goto(-(i / 2), (i / 2) / 3 ** 0.5)
t.down()

for m in range(1, 4):
    flake(i, j)
    t.right(120)

t.update()
t.done()
