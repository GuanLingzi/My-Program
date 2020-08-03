n = '5.5'
n = float(n)
n = int(n)
print(n)

# eval()可以去除数据的外层包裹
n = '3.14'
n = eval(n)
print(n)

# 判断分数等级
score = eval(input('请输入分数：'))
if score > 50:
    print('A')
else:
    print('B')

# 打印0~100以内的所有数之和（两种方法：计数循环和条件循环）
sum_n = 0
for i in range(0, 101):
    sum_n += i
print(sum_n)

# pass保持代码完整性
# continue结束本次循环，不影响后续循环
# break打破循环，跳出循环
# 利用while循环出1~100内所有的偶数
n = 1
while n < 101:
    temp = n % 2
    if temp == 0:
        print(n)

# 打印2~1000内所有的质数
# 一个大于1的数，除了1和本身之外不能被其他自然数整除，那么称它为质数（素数）
for n in range(2, 1001):
    for a in range(2, n):
        if n % a == 0:
            break
    else:
        print("%d是质数" % n)

# 今有鸡、兔同笼，上有三十五头，下有九十四足。问：鸡、兔各几何？答曰：鸡有只、兔有只
for x in range(1, 35):
    y = 35 - x
    if 3 * x + 4 * y == 94:
        print('鸡有%s只，兔子有%s只（x， y）')

# 100元买公鸡（5元1只）、母鸡（3元1只）、小鸡（1元3只）、一共100只鸡，花光一百元，打印出公鸡、母鸡、小鸡各几只（所有可能的结果）
