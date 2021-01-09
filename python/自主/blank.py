nums = input().split()
target = int(input())
l1 = []
for ans1 in nums:
    for ans2 in nums:
        if int(ans1) + int(ans2) == target:
            l1.append(ans1)
            l1.append(ans2)
            break
print(l1)
