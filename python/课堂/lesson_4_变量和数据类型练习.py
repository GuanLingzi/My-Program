# 1.创建变量，提示用户输入数字，变量名为test，变量值为用户输入的数字（要求是必须是数字类型），并输出相应数字。
# eval() 去除数据外层包裹  eval('1')结果为1
test = eval(input('请输入数字：'))
print('您输入的数字是：', test)
# 2.查看下列变量的内存地址和数据类型并将a转换为字符串类型，将b转换为浮点数类型，将c和d转换为整数类型
a = 123
b = '123'
c = b'123'
d = 123.0
print(id(a), id(b), id(c), id(d))
print(type(a), type(b), type(c), type(d))
a1 = str(a)
print(a1)
b1 = float(b)
print(b1)
c1 = int(c)
d1 = int(d)
print(c1, d1)
# 3.建立一个列表，列表内容为0到9十个数字，列表名设置为list_1，并打印此列表
list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_1)
# 4.建立一个元组，元组内容为a、b、c、d、e、f、g七个英文字母，元组名设置为tuple_1，并打印该元组
tuple_1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g')
print(tuple_1)
tuple_3 = tuple('abcdefg')
print(tuple_3)
# 5.将上述列表转换为元组，命名为tuple_2，并输出
tuple_2 = tuple(list_1)
print(tuple_2)
# 6.将上述元组转换为列表，命名为list_2，并输出
list_2 = list(tuple_1)
print(list_2)
