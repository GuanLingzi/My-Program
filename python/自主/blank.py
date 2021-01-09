import random
import time

d = {}
res = []
nums = []
target = random.randint(1, 1000000)
for n in range(1, 1000001):
    nums.append(n)

t0 = time.time()

for idx, i in enumerate(nums):
    diff = target - i
    if i in d:
        res = [d[i], idx]
        break
    else:
        d[diff] = idx
print(res)

t1 = time.time()
print("used time:", t1 - t0, "s")
