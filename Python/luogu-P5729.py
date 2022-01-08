def delete(a, b, c, d, e, f):
    for o in range(c - 1, f):
        for p in range(b - 1, e):
            for r in range(a - 1, d):
                ls[o][p][r] = 0


p_l = input().split()
q = int(input())
s = 0
w, x, h = map(int, p_l)
ls = [[[1 for _ in range(w)] for _ in range(x)] for _ in range(h)]

for i in range(q):
    l1 = input().split()
    x1, y1, z1, x2, y2, z2 = map(int, l1)
    delete(x1, y1, z1, x2, y2, z2)

for g in range(h):
    for i in range(x):
        for j in range(w):
            if ls[g][i][j] == 1:
                s += 1

print(s)
