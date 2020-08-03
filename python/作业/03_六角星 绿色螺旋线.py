import turtle
import time

# 六角星

t = turtle.Pen()
t.speed(0)
t.color(0, 1, 1)
t.pensize(20)
t.fillcolor(0, 1, 1)

t.begin_fill()

t.left(30)
t.forward(144)

t.right(60)
t.forward(144)

t.right(60)
t.forward(144)

t.right(60)
t.forward(144)

t.right(60)
t.forward(144)

t.right(60)
t.forward(144)

t.forward(144)
t.right(120)
t.forward(144)

t.left(60)
t.forward(144)
t.right(120)
t.forward(144)

t.left(60)
t.forward(144)
t.right(120)
t.forward(144)

t.left(60)
t.forward(144)
t.right(120)
t.forward(144)

t.left(60)
t.forward(144)
t.right(120)
t.forward(144)

t.left(60)
t.forward(144)
t.right(120)
t.forward(144)

t.end_fill()

time.sleep(10)
t.reset()

# 绿色螺旋线

t = turtle.Pen()
t.pencolor('green')
turtle.bgcolor('black')
t.speed(0)
sides = 6

for i in range(100):
    t.pensize(i / 50)
    t.forward(i)
    t.left(61)

turtle.done()