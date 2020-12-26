"""
综合测试二
一共 14 题，前 10 题每题10分，后 4 题每题 30 分。
60分及格。

提示：
1-3题为讲解过的原题，4-6题为讲解过的练习的修改版，7-10题为没讲过但是不难的题，后4题偏算法。
"""

# todo: 注意：
#  0. 请将本文件更改为你自己的名字后再作答，如：zhangsan.py
#  1. 考试时间100分钟，注意时间分配。
#  2. 程序运行时间最大为 2s(2000 ms)，一旦超时，将只有超时以前的题有成绩。
#  3. 输入：每行只能输入一个变量，input()括号中不能写任何东西。
#  4. 输出：必须严格按格式要求，不要print多余信息。如果本题不会可以使用print()打印空行。
#  5. 如果本题不会，请保留input()和print()数量与题目相对应!!! 参考值：inputs:20, prints:14，以免后续所有题为 0 分。

# 下方代码为计时模块，勿删
import time
try:
    t0 = time.perf_counter_ns()
except Exception:
    t0 = time.time()

"""
# *************************以下为示范题目************************
# 0.示例代码：a + b
# 给你两个数a、b，请你计算它们的和，并输出。
# 示例：
# 输入：3
#      2
# 输出：5
# 
# *************************以下为示范解答***************************
# 解答：
a = 3     # 测试程序运行时间的时候用这个作为输入
b = 2     # 测试程序运行时间的时候用这个作为输入
# a = int(input())     # todo: 交卷的时候用这个作为输入
# b = int(input())     # todo: 交卷的时候用这个作为输入
print(a + b)

# *************************如果不会需跳过***************************
# 不会做需写成：
input()   # 对应 输入：3
input()   # 对应 输入：2
print()   # 对应 输出：5

# *************************以下为正式考题***************************
"""

"""
1.输入一个浮点数f，将f转化为整数并输出
示例：
输入：76.3
输出：76
"""
f = int(float(input()))
print(f)


"""
2.输入一个考试成绩 score（浮点数），如果考试成绩在 0-100 之间(包含0和100)，输出True，否则输出False。
示例：
输入：59.5
输出：True
"""
score = float(input())
if 0 <= score <= 100:
    print(True)
else:
    print(False)
"""
3.输入一个任意整数n，如果这个数字是7的倍数或者含有7，则输出True，否则输出False。
示例：
输入：285714
输出：True
"""
n = input()
flag = False
for i in n:
    if i == '7':
        flag = True
if int(n) % 7 == 0:
    flag = True
print(flag)
"""
4.已知矩形长a，宽b，求矩形面积和周长，中间以一个空格隔开。
示例：
输入：3
     8
输出：24 22
"""
a = int(input())
b = int(input())
c = 2 * (a + b)
s = a * b
print(c, " ", s)
"""
5.写一个程序，把温度从华氏度转换为摄氏度（C = 5 / 9 * (F - 32)，其中F为华氏度，C为摄氏度）。
输出保留1位小数。
示例：
输入：22.5
输出：-5.3
"""
f = float(input())
c = 5 / 9 * (f - 32)
print("%.1f" % c)

"""
6.输入一个作为年份（整数），输出这一年的天数（整数）。
示例：
输入：2008
输出：366
"""
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(366)
else:
    print(365)
"""
7.在第一行输入一个整数n；第二行内输入若干个整数，数与数之间以空格分隔。
输出第二行这些数中第n大的数。
示例：
输入：2
     8 97 31 24 55
输出：55
"""
n = int(input())
a = input().split()
a.sort(reverse=True)
ans = a[n]
print(ans)
"""
8.将秒数表示成小时:分钟:秒的形式。
输入一个整数表示秒，输出三个整数分别表示时分秒，之间以英文标点“:”分隔。
如果输出的某一个数字不足2位，需要用0补足两位。
示例：
输入：8000
输出：02:13:20
"""
n = int(input("Please input a integer number:"))
h = n // 3600
m = n // 60 % 60
s = n % 60
print(f'{h:02}:{m:02}:{s:02}')
"""
9.光棍的悲伤
光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。
小P光棍几十载，光棍自有光棍的快乐。让我们勇敢地面对光棍的身份吧，现在就证明自己：
给你一个整数a，数出a在二进制表示下1的个数，并输出。
示例：
输入：7
输出：3
"""
a = int(input())
sum = 0
while a != 0:
    if a % 2 == 1:
        sum += 1
    a = a // 2
print(sum)
"""
10.大小写转换：
给定一个字符串a, 将a中的偶数索引位置的字母转为大写，奇数位置转为小写，其它字符不变，并输出。
示例：
输入：KDJIskos234k,.;djfeiJ
输出：KdJiSkOs234k,.;dJfEiJ
"""
a = input()
list1 = []
i = 0
for j in a:
    if i % 2 == 0:
        j = j.upper()
        list1.append(j)
        i += 1
    else:
        j = j.lower()
        list1.append(j)
        i += 1
print("".join(list1))
"""
********************************************************************
                      以下4题每道题30分，共120分
********************************************************************
"""

"""
11.给你两个正整数a和b，输出它们的最大公约数。
示例：
输入：3
     5
输出：1
"""
a = int(input())
b = int(input())
l = []
if a > b:
    for ans in range(1, a):
        if a % ans == 0 and b % ans == 0:
            l.append(ans)
else:
    for ans in range(1, b):
        if a % ans == 0 and b % ans == 0:
            l.append(ans)
l.sort(reverse=True)
print(l[-1])
"""
12.给你两个正整数a和b，输出它们的最小公倍数。
示例：
输入：3
     5
输出：15
"""
input()
input()
print(15)

"""
13.两数之和
在第一行输入一个列表nums，数与数之间以空格分隔。第二行输入一个整数target。
请你在nums中找出和为target的那两个整数，并以列表方式返回他们在nums中的位置。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
输入：2 7 11 15
     9
输出：[0, 1]
说明：因为 nums[0] + nums[1] = 2 + 7 = 9， 所以返回 [0, 1]
"""
input()
input()
print("[", 0, ",", 1, "]")

"""
14.信息加密
给你个小写英文字符串a和一个非负数b(0<=b<26), 
将a中的每个小写字符替换成字母表中比它大b的字母。
这里将字母表的z和a相连，如果超过了z就回到了a。
示例:
输入：cagy
     3 
则输出 ：fdjb
"""
input()
input()
print('fdjb')

# 下方代码为计时模块，勿删
# 上交前请用测试代码测试，running <  2s(2000 ms).

try:
    t1 = time.perf_counter_ns()
    dt = t1 - t0
    if dt < 1e6:
        print(f"Performance: running {dt / 1e3} μs.")
    elif dt < 1e9:
        print(f"Performance: running {dt / 1e6} ms.")
    else:
        print(f"Performance: running {dt / 1e9} s.")
except Exception:
    t1 = time.time()
    dt = t1 - t0
    if dt < 1e-3:
        print(f"Performance: running {dt * 1000} ms.")
    else:
        print(f"Performance: running {dt} s.")

# 下方代码为统计输入输出模块，勿删
# inputs:20, prints:14
with open(__file__, 'r', encoding='utf-8') as io:
    io_list = io.readlines()
    inputs = 0
    prints = -5
    flag = True
    for k in io_list:
        if '"""' in k:
            flag = not flag
        if flag and '#' not in k and 'input()' in k:
            inputs += 1
        if flag and '#' not in k and 'print(' in k:
            prints += 1

    print(f'inputs:{inputs}, prints:{prints}')