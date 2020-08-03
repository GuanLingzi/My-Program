# # 简化前
# num = int(input("num:"))
# cnt = 2
# is_prime = True

# while cnt < num:
#     if num % cnt == 0:
#         is_prime = False
#         break
#     cnt += 1

# if is_prime:
#     print("yes")
# else:
#     print("no")

# # 简化后
# num = int(input("num:"))
# is_prime = True

# # for i in range(2, num):
# for i in range(2, int(num ** 0.5)):
#     if num % i == 0:
#         print("no")
#         break
# else:
#     print("yes")

ball_height = 100
total = ball_height
n = int(input('请输入弹几次：'))

for i in range(1, n + 1):
    if i == n:
        break
    else:
        ball_height /= 2
        total = total + ball_height * 2
print(total)
