import time
t0 = time.time()


def primes_set(n):
    # 1.初始化
    bls = [0, 1] * (n // 2)
    bls[1], bls[2] = 0, 1

    # 2.倍数置0
    for idx in range(3, n):
        if bls[idx]:
            for j in range(idx * idx, n, idx * 2):
                bls[j] = 0

    # 3.加入素数表
    prime_set = set()
    for idx in range(n):
        if bls[idx]:
            prime_set.add(idx)

    return prime_set


def is_bprime_set(n, prime_set):
    for p in range(2, int(n ** 0.5) + 1):
        q = n / p
        if p in prime_set and q in prime_set:
            return n
    return False


def bprimes_set(a, b):
    if a < 4:
        a = 4

    prime_set = primes_set(b)

    bprime_list = []
    for i in range(a, b):
        bprime = is_bprime_set(i, prime_set)
        if bprime:
            bprime_list.append(bprime)
    return bprime_list


print(len(bprimes_set(1, 1000000)))
t1 = time.time() - t0
print(f"used time: {t1} s.")
