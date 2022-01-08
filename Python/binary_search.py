# import random as r
#
# ran_int = r.randint(0, 100)
#
# while True:
#     in_int = int(input())
#     if in_int > ran_int:
#         print("it's too large.")
#     elif in_int < ran_int:
#         print("it's too small.")
#     else:
#         print("you're right.")
#         break
def bi(l1, t):
    mn = l1[0]
    mx = l1[-1]
    mid = len(ls) // 2
    while True:
        if ls[mid] > t:
            mx = mid - 1
            mid //= 2
        elif ls[mid] < t:
            mn = mid + 1
            mid //= 2 + mid * 2
        else:
            if ls[mid] == t:
                return mid
            else:
                return -1


ls = [1, 3, 7, 9, 13]
target = 70
print(bi(ls, target))
