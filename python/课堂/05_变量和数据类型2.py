import keyword

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)

print(keyword.kwlist)

zhangsan_chinese_score = float(input('请输入张三的语文成绩：'))
zhangsan_maths_score = float(input('请输入张三的数学成绩：'))

print(type(zhangsan_chinese_score))
print(type(type(zhangsan_chinese_score)))

print('''The weather 
is clear today''')

str1 = '''今天的天气：
        晴转多云'''
print(str1)

str2 = input('请输入：')
print(str2)

price = float(input('请输入单价（元/斤）：'))
weight = float(input('请输入重量（斤）：'))
apple = price * weight
print('您共需付款：', apple, '元')

base = 1500
price = float(input('请输入相机单价：'))
price = 0.02 * price
camera_num = float(input('请输入一共买了几台相机：'))
bonus = 200 * camera_num
total = base + price * camera_num + bonus

print('您的薪资是：', total, '元')
