import turtle

t = turtle.Pen()
t.penup()

for i in range(4):
    t.forward(20)
    t.pendown()
    t.forward(40)
    t.penup()
    t.forward(20)
    t.right(90)

turtle.done()
