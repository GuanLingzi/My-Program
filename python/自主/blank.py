# Load the module
import time
import random

# Place your code here
d = {}
res = []
nums = []

result = input("Do you want to customize the length？（'y' or 'n'):")
if result == "y":
    n = int(input("Please input a integer:"))
    print("The length is:", n, "\n")
    time.sleep(2)
elif result == 'n':
    print("The length will be randomly selected between 1000000 and 100000000.\n")
    n = random.randint(1000000, 100000000)

# Start the timing
t0 = time.time()

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
print("Index of the same value is:", res)

if result == 'n':
    print("Used length:", n)

# Stop the timing
t1 = time.time()
# Output the time
print("Used time:", t1 - t0, "s")
