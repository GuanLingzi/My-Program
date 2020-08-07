# =========学员管理系统========
# 输入'1': 添加学号、姓名和成绩
# 输入'2': 根据学号删除学员信息
# 输入'3': 根据学号修改学员信息
# 输入'4': 根据学号查询学员信息
# 输入'5': 查询所有学员信息
# 否则输入任意字符退出
# =============================

# 循环，条件判断，列表
# 学号、姓名和成绩
# 列表嵌套，大列表当中存放小列表

students = []  # 大列表
while True:
    student_img = []  # 小列表
    title = """
=========学员管理系统========
输入'1': 添加学号、姓名和成绩
输入'2': 根据学号删除学员信息
输入'3': 根据学号修改学员信息
输入'4': 根据学号查询学员信息
输入'5': 查询所有学员信息
否则输入任意字符退出
============================= """

    print(title)
    select = input('请输入您的选项:')  # 输入的一定是字符串
    if select == '1':
        student_img.append(eval(input('请输入学生学号:')))
        student_img.append(input('请输入学生姓名:'))
        student_img.append(eval(input('请输入学生成绩:')))
        students.append(student_img)
        # pass保证程序正常运行
    elif select == '2':
        stu_id = eval(input('请输入学生学号:'))
        for stu_res in students:
            if stu_res[0] == stu_id:
                print('{}学员信息已删除'.format(stu_res))
                students.remove(stu_res)
                break
        else:
            print('该学生不存在或已删除')
    elif select == '3':
        stu_id = eval(input('请输入学生学号:'))
        for stu_res in students:
            if stu_res[0] == stu_id:
                stu_res[0] = eval(input('请输入修改后的新学号:'))
                stu_res[1] = input('请输入修改后的姓名:')
                stu_res[2] = eval(input('请输入修改后的成绩:'))
                break
        else:
            print('查无此人，如需添加请按1')
    elif select == '4':
        stu_id = eval(input('请输入学生学号:'))
        for stu_res in students:
            if stu_res[0] == stu_id:
                print('该学生信息为:', stu_res)
                break
        else:
            print('查无此人，如需添加请按1')
    elif select == '5':
        if len(students) == 0:
            print('暂无学员信息，如需添加请按1')
        else:
            print('当前所有学生信息为:', students)
    else:
        print('输入不合法，程序退出')
        break
