names = []
scores = []
main = """
=========【学员管理系统】beta========
输入'1': 增加学生信息
输入'2': 删除学生信息
输入'3': 查询所有学生信息
输入'4': 根据学生姓名查找成绩
输入'5': 根据学生姓名修改成绩
输入'0': 退出
===================================="""
exit_title = """
================
谢谢使用本系统
系统已退出
================"""
while True:
    print(main)
    a = int(input("请输入操作序号："))
    if a == 1:
        name1 = input("请输入姓名：")
        if name1 in names:
            print("已存在该姓名")
            continue
        else:
            score1 = input("请输入成绩：")
            names.append(name1)
            scores.append(score1)
    elif a == 2:
        name2 = input("请输入姓名：")
        if name2 in names:
            b = names.index(name2)
            names.pop(b)
            scores.pop(b)
            # del names[b]
            # del scores[b]
            print("已成功删除")
        else:
            print("查无此人，如需添加请按1")
    elif a == 3:
        for i in names:
            c = names.index(i)
            print(i, scores[c])
    elif a == 4:
        name4 = input("请输入姓名：")
        if name4 in names:
            d = names.index(name4)
            print(scores[d])
        else:
            print("查无此人，如需添加请按1")
    elif a == 5:
        name5 = input("请输入姓名：")
        if name5 in names:
            e = name5.index(name5)
            score5 = input("输入修改成绩：")
            scores[e] = score5
            print("修改成功")
        else:
            print("查无此人，如需添加请按1")
    elif a == 0:
        print(exit_title)
        break
    else:
        print("输入不合法，请重新输入")
