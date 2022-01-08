def hail(n):
    l1 = [n]
    while n != 1:
        if n % 2 != 0:
            n = 3 * n + 1
            l1.append(n)
        else:
            n //= 2
            l1.append(n)
    d1 = {'数字': l1[0], '变换次数': len(l1) - 1, '最大值': max(l1), '过程': l1}
    return d1


def bubble_sort(n, b):
    x = 0
    for k in range(len(n) - 1 - x):
        for i in range(len(n) - 1):
            if b:
                if n[i]['变换次数'] < n[i + 1]['变换次数']:
                    n[i], n[i + 1] = n[i + 1], n[i]
                    x += 1
                else:
                    continue
            else:
                if n[i]['变换次数'] > n[i + 1]['变换次数']:
                    n[i], n[i + 1] = n[i + 1], n[i]
                    x += 1
                else:
                    continue
    return n


reverse = bool(input("Do you want to reverse?(True or False):"))
ls = []
for s in range(2, 1000):
    ls.append(hail(s))
ls = bubble_sort(ls, reverse)
for a in ls:
    print(a)
