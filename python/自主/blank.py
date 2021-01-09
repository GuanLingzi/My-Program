# Load the module
import time
import random

# Start the timing
t0 = time.time()

# Place your code here
d = {}
res = []
nums = []
target = random.randint(1, 1000000)
for n in range(1, 1000001):
    nums.append(n)

for idx, i in enumerate(nums):
    diff = target - i
    if i in d:
        res = [d[i], idx]
        break
    else:
        d[diff] = idx
print(res)

# Stop the timing
t1 = time.time()
# Output the time
print("used time:", t1 - t0, "s")
