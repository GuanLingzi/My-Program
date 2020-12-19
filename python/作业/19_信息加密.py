# 本周作业
c = ""
a = input("Please input a lower English string:")
b = int(input("Please input a integer:"))
for j in a:
    if ord(j) + b <= ord('z'):
        c += chr(ord(j) + b)
    else:
        c += chr(ord(j) - 26 + b)
print(c)
# 回文数那个
l1 = [2]
l2 = []
for i in range(2, 1000):
    for n in range(2, i):
        if i % n == 0:
            break
        elif (i - 1) == n:
            l1.append(i)

for j in l1:
    j = str(j)
    if j == j[::-1]:
        l2.append(int(j))
print(l2)
