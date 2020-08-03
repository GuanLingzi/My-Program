import turtle

t = turtle.Pen()

name = input('请输入姓名：')
gender = input('请输入性别：')
age = int(input('请输入年龄：'))
height = float(input('请输入身高（m）：'))
weight = float(input('请输入体重（kg）：'))

BMI = weight / (height ** 2)

print('''BMI指数表
         小于 18.5 偏瘦
         18.5 - 23.9 正常
         大于等于 24 超重
         24 - 26.9 偏胖
         27 - 29.9 肥胖
         大于等于 30 重度肥胖
         大于等于 40 极重度肥胖''')
print('您的BMI指数为:', BMI, '性别:', gender)

n1 = str(name)
n2 = int(name)
n3 = float(name)
n4 = bool(name)
print(n1, n2, n3, n4)

g1 = str(gender)
g2 = int(gender)
g3 = float(gender)
g4 = bool(gender)
print(g1, g2, g3, g4)

a1 = str(age)
a2 = int(age)
a3 = float(age)
a4 = bool(age)
print(a1, a2, a3, a4)

h1 = str(height)
h2 = int(height)
h3 = float(height)
h4 = bool(height)
print(h1, h2, h3, h4)

w1 = str(weight)
w2 = int(weight)
w3 = float(weight)
w4 = bool(weight)
print(w1, w2, w3, w4)

for i in range(5):
    t.forward(100)
    t.left(360 / 5)
turtle.done()

for i in range(6):
    t.forward(100)
    t.left(360 / 6)
turtle.done()

s = int(input('请输入你要画几边形：'))
for i in range(s):
    t.forward(100)
    t.left(360 / s)
turtle.done()
