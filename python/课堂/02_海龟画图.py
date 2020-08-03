import turtle

print(3 + 5)
print(10 - 2)
print(13 * 25)
print(75 / 3)
print(9 / 2)
print(3.5 / 1.2)
print(1 / 3)
print(12345 * 54321)
print(3 + 5 * 2)
print(3 + 4)
print(5 - 2)
print(5 * 2)
print(7 / 3)
print(3 ** 3)

a = 8
a += a + 1
print(a)

b = 8
b -= b + 1
print(b)

a = 12.5
b = 16.7
c = a * b
print('此房间的周长是：', c)

f = float(input('请输入华氏度:'))
c = 5 / 9 * (f - 32)
print('您输入的华氏度转换为摄氏度是：', c)

a = float(input('语文成绩是：'))
b = float(input('数学成绩是：'))
c = a + b
d = (a + b) / 2
print('您的总分是：', c, '平均分是：', d)


t = turtle.Pen()
t.backward(100)
t.dot(20)
t.penup()
t.right(90)
t.forward(20)
t.pendown()
t.circle(15)
t.forward(100)
turtle.done()
