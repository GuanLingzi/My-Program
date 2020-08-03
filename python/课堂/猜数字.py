import random
import turtle

t = turtle.Pen()
turtle.setup(width=330, height=200, startx=0, starty=0)
turtle.bgcolor('green')
t.hideturtle()
t.color('white')
t.penup()
t.setpos(-100, 50)
my_font = ('黑体', 16)
t.write('请输入您猜的数字！', font=my_font)
target_num = random.randint(1, 100)
while True:
    guess_num = turtle.simpledialog.askinteger('猜数游戏', '请输入1~100之间的一个数(不要按0，会退出）： ')
    if guess_num == target_num:
        t.clear()
        t.setpos(-100, 0)
        t.write('你猜对了，游戏结束。', font=my_font)
        break
    elif not guess_num:
        t.clear()
        t.setpos(-100, 0)
        t.write('你放弃了，游戏结束。', font=my_font)
    elif guess_num > target_num:
        t.clear()
        t.write('你猜大了，再猜一次： ', font=my_font)
    else:
        t.clear()
        t.write('你猜小了，再猜一次： ', font=my_font)
turtle.done()
