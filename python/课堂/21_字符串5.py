a = input("please input:")
b = []

for i in a:
    if i == "(":
        b.append(i)
    if i == ")":
        if b:
            b.pop()
        else:
            b = bool(b)
            b = True
            break

if b:
    print("False")
else:
    print("True")
