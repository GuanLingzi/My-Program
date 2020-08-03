import re

post = input('请输入邮件重量及是否加急（用空格分隔 y 为加急 n 为不加急)：')
emergency = ''.join(re.findall(r'[A-Za-z]', post))
post_height = int(re.sub("\D", "", post))

if post_height >= 0:
    if post_height <= 1000:
        if emergency == 'y':
            total = 13
            print('total:', total)
        else:
            total = 8
            print('total:', total)
    else:
        if emergency == 'y':
            total = 8 + 5 + (post_height - 1000) / 500 * 4
            print('total:', total)
        else:
            total = 8 + (post_height - 1000) / 500 * 4
            print('total:', total)
else:
    print('输入不合法')
