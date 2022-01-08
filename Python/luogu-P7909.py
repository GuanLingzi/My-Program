# def candy(p, mn, mx):
#     out = 0
#     if 2 <= p <= mn <= mx:
#         for k in range(mn, mx + 1):
#             if k % p > out:
#                 out = k % p
#     return out
def candy(p, mn, mx):
    a = mn - mn % p + n
    if mx >= a:
        out = n - 1
    else:
        out = mx % p
    return out


n, L, R = map(int, input().split())
print(candy(n, L, R))
