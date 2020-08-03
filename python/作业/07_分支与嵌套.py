import random
# 电脑只会出石头
computer_output = 1
main = '''
请输入你要出什么
石头 - 1
剪刀 - 2
布 - 3'''
print(main)

while True:
    human_output = int(float(input('请输入你要出什么:')))
    if 0 < human_output < 4:
        if human_output == computer_output:
            print('平局')
        elif human_output - computer_output == 1:
            print('电脑赢')
        else:
            print('您赢了！')
    else:
        print('输入不合法，请重新输入')

# 电脑随机出
computer_output = random.randint(1, 3)
main = '''
请输入你要出什么
石头 - 1
剪刀 - 2
布 - 3'''
print(main)

while True:
    human_output = int(float(input('请输入你要出什么:')))
    if 0 < human_output < 4:
        if human_output < computer_output or human_output == computer_output + 2:
            print('你赢了')
        elif human_output == computer_output:
            print('平局')
        else:
            print('电脑赢')
