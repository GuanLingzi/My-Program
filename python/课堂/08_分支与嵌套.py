money = float(input('请输入金额：'))
dis1 = 0.1
dis2 = 0.2

if money <= 10:
    price = money - dis1 * money
    print('您的折扣是:', dis1 * 100, '%', '，共需付：', price, '元')
else:
    price = 10 - dis1 * 10 + (money - 10) * (1 - dis2)
    print('您的折扣是:', dis2 * 100, '%', '，共需付：', price, '元')

score = float(input('请输入分数：'))

if 0 < score < 100:
    if score >= 90:
        print('优')
    elif score >= 80:
        print('良')
    elif score >= 70:
        print('中')
    elif score >= 60:
        print('及格')
    else:
        print('不及格')
else:
    print('输入不合法')

year = int(float(input('请输入年份：')))
month = int(float(input('请输入月份：')))

if 0 < month < 12 and year != 0:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print('本月有31天')
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print('本月有30天')
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print('本月有29天')
    else:
        print('本月有28天')
else:
    print('输入不合法')
