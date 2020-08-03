# 1
num = int(input("请输入数字："))

if num > 1:
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                print(" %d 是合数！" % num)
                break
            else:
                print(" %d 是素数（质数）！" % num)
    else:
        print(" %d 是素数（质数）！" % num)
else:
    print("输入不合法！")

# 2
post_weight = float(input('请输入邮件重量：'))
emergency = input('请输入是否加急（y 加急 n 不加急）：')

if post_weight >= 0:
    if post_weight <= 1000:
        if emergency == 'y':
            total = 13
            print('total:', total)
        else:
            total = 8
            print('total:', total)
    else:
        if emergency == 'y':
            total = 8 + 5 + ((post_weight - 1000) // 500 + 1) * 4
            print('total:', total)
        else:
            total = 8 + ((post_weight - 1000) // 500 + 1) * 4
            print('total:', total)
else:
    print('输入不合法')
