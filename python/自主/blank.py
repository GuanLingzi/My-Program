# Load the module
import time
import random

# Start the timing
t0 = time.time()

# Place your code here
n = random.randint(1000000, 100000000)
d = {}
res = []
nums = []
target = random.randint(1, n)
for n in range(1, n + 1):
    nums.append(n)

for idx, i in enumerate(nums):
    diff = target - i
    if i in d:
        res = [d[i], idx]
        break
    else:
        d[diff] = idx
print(res)
print("Used length:", n)

# Stop the timing
t1 = time.time()
# Output the time
print("Used time:", t1 - t0, "s")
