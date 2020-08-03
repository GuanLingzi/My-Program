import turtle

t = turtle.Pen()
t.speed(0)

for i in range(400):
    t.forward(100)
    t.right(90)
turtle.done()

s = float(input('请输入你要画几边形：'))
for i in range(s):
    t.forward(100)
    t.left(360 / s)
turtle.done()

for i in range(5):
    t.forward(100)
    t.left(144)

t.pencolor(0, 1, 1)
for i in range(1, 999999):
    t.forward(i)
    t.left(90)
turtle.done()
