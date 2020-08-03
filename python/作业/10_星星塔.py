# 修改前
n = int(input("请输入几层："))
star = '*'

if n >= 1:
    for i in range(1, n + 1):
        print(star * i)
else:
    print("输入不合法")

# 修改后
print('*')
print('**')
print('***')
print('****')
print('*****')

# 再次修改
n = int(input("请输入几层："))
star = '*'

if n >= 1:
    for i in range(1, n + 1):
        for a in range(i):
            print(star, end='') 
        print('')
else:
    print("输入不合法")
