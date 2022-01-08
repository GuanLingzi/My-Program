def primes(n):
    # 1.初始化
    bls = [0, 1] * (n // 2 + 1)
    bls[1], bls[2] = 0, 1

    # 2.倍数置0
    for idx in range(3, int(n**0.5)+1):
        if bls[idx]:
            for j in range(idx * idx, n, idx * 2):
                bls[j] = 0

    # 3.加入素数表
    prime_list = []
    for idx in range(n):
        if bls[idx]:
            prime_list.append(idx)

    return prime_list

import time
n = 1000000
t = time.time()
prime_list = primes(n)
t = time.time() - t
print(len(prime_list))
print("used time:", t, "s.")
