import time


def euler():
    # TODO: 27 ** 5 + 84 ** 5 + 110 ** 5 + 133 ** 5 = 144 ** 5
    l1 = []
    for i in range(1, 150):
        i = i ** p
        l1.append(i)
    s1 = set(l1)
    for a in range(len(s1)):
        for b in range(a + 1):
            for c in range(b + 1):
                for d in range(c + 1):
                    s = a + b + c + d
                    if s in s1:
                        return l1.index(a) + 1, l1.index(b) + 1, l1.index(c) + 1, l1.index(d) + 1, l1.index(s) + 1


p = 5
t0 = time.time()
print(euler())
t1 = time.time() - t0
print(f"used time:{t1}s.")
