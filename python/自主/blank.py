a = int(input())
b = int(input())
l = []
if a > b:
    for ans in range(1, a):
        if a % ans == 0 and b % ans == 0:
            l.append(ans)
else:
    for ans in range(1, b):
        if a % ans == 0 and b % ans == 0:
            l.append(ans)
l.sort(reverse=True)
print(l[-1])
