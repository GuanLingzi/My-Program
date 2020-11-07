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
