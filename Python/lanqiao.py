s = input()
l = []
sum = 0
for i in s:
    if type(i) == 'class<int>':
        l.append(int(i))
l.sort()
print(l)
for k in range(0, len(l) - 1):
    if l[k] == l[k + 1]:
        sum += 1
print(sum)
