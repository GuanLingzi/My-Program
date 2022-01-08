def p2141(ls):
    s = set(ls)
    sum = 0
    for i in s:
        if i > n:
            for j in s:
                c = i - j
                if c in s:
                    sum += 1
                    break
    return sum


n = int(input())
a = input()
ls_b = []
for i in a:
    ls_b.append(int(i))
print(p2141(ls_b))
