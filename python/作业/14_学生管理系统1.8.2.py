# Student Achievement Management System
name_list = []
main = """
===================================
Welcome to [Student Achievement Management System] v1.8.2

1: Add student information
2: Delete student information
3: Query all student information
4: Find grades based on student names
5: Modify the grades according to the student's name

0: exit
===================================="""
exit_title = """
====================================
Thank you for using this system
The system has exited
===================================="""
while True:
    print(main)
    a = int(input("Please enter a number："))
    if a == 1:
        name = input('name:')
        gender = input('gender:')
        score = input('score:')
        person = (name, gender, score)
        name_list.append(person)
    elif a == 2:
        find = input('delete who:')
        i = 0
        for name in name_list:
            if name[0] == find:
                k = input(f"is this person?：{name}('y' or other word):")
                if k == 'y':
                    name_list.pop(i)
                    print('deleted successfully!')
                else:
                    print('Keep looking for the next one')
            i += 1
    elif a == 3:
        for name in name_list:
            print(f"name:{name[0]} gender:{name[1]} score:{name[2]}")
    elif a == 4:
        find = input('find who:')
        i = 0
        for name in name_list:
            if name[0] == find:
                k = input(f"is this person?：{name}('y' or other word):")
                if k == 'y':
                    print(f"name:{name[0]} gender:{name[1]} score:{name[2]}")
                else:
                    print('Keep looking for the next one')
            i += 1
    elif a == 5:
        find = input('change who:')
        i = 0
        for name in name_list:
            if name[0] == find:
                k = input(f"is this person?：{name}('y' or other word):")
                if k == 'y':
                    print(f"name:{name[0]} gender:{name[1]} score:{name[2]}")
                    name_list[i] = list(name)
                    name = name_list[i]
                    name[0] = input('new name:')
                    name[1] = input('new gender:')
                    name[2] = input('new score:')
                    name_list[i] = tuple(name_list)
                    print('changed successfully')
                else:
                    print('Keep looking for the next one')
            i += 1
    elif a == 0:
        print(exit_title)
        break
    else:
        print("Input error, re-enter")
