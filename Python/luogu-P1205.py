def right90(e_l):
    t_l = e_l
    for j in range(n):
        for k in range(n):
            e_l[j][k] = t_l[k][j]
    return t_l


n = int(input())
start_l = []
end_l = []

for i in range(n):
    a = input().split(' ')
    start_l.append(a)
for i in range(n):
    a = input().split(' ')
    end_l.append(a)

print(right90(end_l))
