a = input("请输入一串字符（只限大小写英文）：")
a = list(a)
b = len(a)
for i in range(b):
    for j in a:
        if i % 2 == 0:
            a[i] = j.upper()
        else:
            a[i] = j.lower()
a = str(a)
print(a)
