import turtle

# turtle 乌龟  import 引入
t = turtle.Turtle(shape='turtle')
for i in range(4):
    t.forward(100)
    t.right(90)

# 画六边形
for i in range(6):
    t.forward(100)
    t.right(60)

# 画棒棒糖
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
t.color(colors[3])
for i in range(200):
    t.forward(i)
    t.right(60)

# 画五彩螺旋
for i in range(100):
    t.pencolor(colors[i % 6])
    t.forward(i)
    t.right(60)

# 海龟下蛋
turtle.bgcolor('black')
for i in range(300):
    t.pencolor(colors[i % 6])
    t.penup()
    t.forward(i)
    t.pendown()
    t.dot(6)
    # t.write('g', font=('微软雅黑', 20))
    t.width(i / 100 + 1)
    t.right(61)
turtle.done()
