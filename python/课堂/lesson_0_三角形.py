import turtle

turtle.pencolor('black')
turtle.bgcolor('white')
turtle.pensize(1)
turtle.pendown()
for i in range(50):
    turtle.forward(10 * i)
    turtle.right(90)
# turtle.done()
turtle.pencolor('black')
turtle.bgcolor('white')
turtle.pensize(10)
turtle.pendown()
for i in range(3):
    turtle.forward(130)
    turtle.left(120)
for i in range(50):
    turtle.forward(10 * i)
    turtle.right(90)
turtle.done()
