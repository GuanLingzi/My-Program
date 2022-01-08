import time


def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


in_1 = 100001651
in_2 = 100001652

t0 = time.time()

ans = gcd(in_1, in_2)

t1 = time.time() - t0

print(ans)
print("used time:", t1 * 1000, 'ms.')
