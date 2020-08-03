# 1
apple_number = int(float(input('请输入吃了几个苹果(只能在0-100之间）：')))

if 0 <= apple_number <= 100:
    if apple_number == 0:
        print('Today,I ate %d apple.' % apple_number)
    elif apple_number == 1:
        print('Today,I ate %d apple.' % apple_number)
    else:
        print('Today,I ate %d apples.' % apple_number)
else:
    print('输入不合法')

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
            total = 8 + 5 + (post_weight - 1000) / 500 * 4
            print('total:', total)
        else:
            total = 8 + (post_weight - 1000) / 500 * 4
            print('total:', total)
else:
    print('输入不合法')
