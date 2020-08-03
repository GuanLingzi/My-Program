# f-string语法格式:
name = "Xiao Ming"
age = 12

print(f"My name is {name}, and I'm {age} years old.")

no = 13
print(f'My no. is |{no:6}|')

price = 9.5
print(f'apple price is {price:.2f}')

name = input('name:')
student_no = int(input('student_no:'))
print(f'my name is {name}, my no. is {student_no:06}.')

price = float(input('price:'))
weight = float(input('weight:'))
print(f'苹果单价{price:.2f}, 重量是{weight:.2f}. 总价是{price * weight:.2f}')

boy = 45
total = 100
print(f'班里男孩比例是{boy / total:.2%}')

num = 1

while num <= 5:
    print('hello Python')
    num += 1

print('循环结束后的 num = %d' % num)

num = 0
sum = 0

while num <= 100:
    sum = sum + num
    num += 1
print(sum)

num = 0
while num <= 100:
    if num % 3 != 0:
        print(num)
        num += 1
    else:
        num += 1

num = 10
while 10 >= num and num<= 100 :
    if num % 3 != 0 and num % 10 != 3 and num // 10 != 3:
        print(num)
    num += 1
