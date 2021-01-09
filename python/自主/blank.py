nums = input().split()
target = int(input())

for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if int(nums[i]) + int(nums[j]) == target:
            print([i, j])
            break
