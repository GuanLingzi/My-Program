name = '关凌梓'
age = 13
height = 163.4

print('my name is %s,my age are %03d,my height are %.2f' % (name, age, height))

name = input('请输入姓名：')
student_no = int(input('请输入学号：'))
price = float(input('请输入价格(元/斤)：'))
weight = float(input('请输入重量(斤)：'))
money = float(price * weight)
scale = float(45)

print('大家好，我的名字叫%s!' % name)
print('我的学号是%06d' % student_no)
print('苹果单价%.2f元/斤，购买了%.2f斤，需要支付%.2f元' % (price, weight, money))
print('班里男生比例是%.2f%%' % scale)

score = float(input('请输入分数：'))

if score >= 90:
    print('可以出去玩')
else:
    print('在家补作业')


score = float(input('请输入分数：'))

if score > 70:
    if score > 80:
        if score > 90:
            print('优')
    else:
        print('良')

print('1')

