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
