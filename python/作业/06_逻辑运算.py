# 1
score = int(float(input('请输入成绩：')))

if score >= 0:
    if score <= 100:
        print('分数正确')
    else:
        print('分数错误，确保分数在0-100之间！')
else:
    print('分数错误，确保分数在0-100之间！')

# 2
python_score = int(float(input('请输入python成绩：')))
math_score = int(float(input('请输入数学成绩：')))

if python_score >= 60:
    if math_score >= 60:
        print('合格')
    else:
        print('不合格')
else:
    print('不合格')

# 3

is_candidate = bool(float(input('请输入您是不是考生，如是，请输入 1 ，如不是，请输入 0 ：')))
if is_candidate:
    print('您是考生')
else:
    print('您不是考生')
