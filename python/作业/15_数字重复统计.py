import random
# 上周作业
a = []
for i in range(1000):
    a.append(random.randint(20, 100))

b = sorted(a)
c = dict()
for i in b:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print(c)
# 这周作业
d = {"张三": 97, "李四": 59, "王五": 100}
