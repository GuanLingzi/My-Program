# python中数据类型分为数字类型、序列类型和其他类型，总之，python中一切皆有类型
# 数字类型分为：整数类型（Int）、浮点型（Float）、复数类型（Complex）、布尔型（Boll）和其他数字类型（Decimal类型和分数类型）。
# 序列类型分为：字符串（str）、元组类型（tuple）、字节序列（bytes）、列表（list）和字节数组（bytearray）。
# 其他类型包括：集合数据类型（set）、字典数据类型（dict）、python一切皆有类型。
# 整数类型int（用于表示整数）、浮点数类型float（用于表示小数）、字符串类型str（用于表示字符串）、布尔型bool（用于表示逻辑真假）。
type(123)
print(type(123))
# python 中提供了函数type（），括号内填写想要查看的变量（值），运用这个函数我们可以知道一个变量的类型。
print(type(90))
num = 89
type_1 = type(num)  # 将判断出的数据类型赋值给变量type_1
print(type_1)  # 打印判断出的数据类型
num_str = '123456789'
type_2 = type(num_str)  # 黄色波浪线代表代码不规范，红色代表代码错误
print(type_2)
# 栗子_1
a = 6.19
type_3 = type(a)
print(type_3)
# 栗子_2
n = True  # True 代表的是数字中的1
type_4 = type(n)
print(type_4)
# 数据类型的相互转换
a = 24
b = float(a)  # 将整数转化为浮点数
print(a, b)
c = 38.0
d = int(c)
print(c, d)
e = 54.99
f = int(e)  # 将浮点数转换为整数，去掉小数点后的部分
print(e, f)
h = "76.3"
i = float(h)  # 将字符串转换为浮点数
print(h, i)
# 数据类型的相互转换：str（）、int（）、float（）、list（）、tuple（）
# 1. float（） 从一个字符串或整数创建一个新的浮点数（小数）
# 2. int（） 从一个字符串或浮点数创建一个新的整数
# 3. str（） 从一个数（或者其他类型）创建一个新的字符串
# 4. list（） 将括号内数据转换为列表
# 5. tuple（） 将括号内数据转换为元组

# 练习：输入数据（请输入数据：），判断这个数据的id地址和数据类型
type_5 = input('请输入数据：')
print(id(type_5))
print(type(type_5))
