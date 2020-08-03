'''# 笔记记法：
【...】：
           【...】：
                  .........
                  .......
           【...】：
                  .........
                  .......
数据类型：
        数字型：
              num
        非数字类型：
                  str
                  list
                  tuple
                  dict
                  set
列表：
    列表的定义：
            最频繁
            一串有序的信息
            用 [] 定义
            索引从0开始
            不能超出索引范围
    列表
增删查改'''

# 列表定义
# 1.班级里有三个学生，放在name_list名册里
name_list = ['古哲', '施意', '杜子腾']
# 2.班级里转来一个学生，把这个人加到名册里
name_list.append('李名哲')
print(name_list)
# 3.定义医院列表
hospital = []
# 4.第一个进班级的人骨折了，被送进了医院
    # 1
        '''del name_list[0]
        print(name_list)'''
    # 2
        '''name_list.remove('古哲')
        print(name_list)'''
    # 3
        '''name_list.pop('古哲')
        print(name_list)'''
    # 4
        '''leave = name_list.pop(0)
        hospital.append(leave)
        print(name_list)
        print(hospital)'''
