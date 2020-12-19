a = input("please input:")
b = False
cnt = 0
# for j in a:
#     if 碰到左括号:
#         cnt += 1
#     elif 碰到右括号:
#         if cnt < 1:
#             break
#         else:
#             cnt -= 1
#     else:
#         继续判断
#
# if cnt == 0:
#     print('算式没问题')
# else:
#     print('算式需修改')

for j in a:
    if j == "(":
        cnt += 1
    elif j == ")":
        if cnt < 1:
            break
        else:
            cnt -= 1
    else:
        continue

if cnt == 0:
    print("True")
else:
    print("False")
