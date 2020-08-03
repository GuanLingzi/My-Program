# 创建空列表
prime_list = []
# 2判断不出，手动加入
prime_list.append(2)
# 判断素数
for j in range(2, 101):
    for i in range(2, j):
        if j % i == 0:
            break
        elif (j - 1) == i:
            # 如果此数是素数，将它加入列表
            prime_list.append(j)
# 打印列表
print(prime_list)
# 定义max,n
m = len(prime_list)
n = int(input("请输入你要访问第几个素数,共%d个：" % m))

# 输出
if 0 < n <= m:
    print(prime_list[n - 1])
else:
    print("输入不合法，请重新输入")
