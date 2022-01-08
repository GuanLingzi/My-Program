# first

# def find_min(l1):
#     a = 0
#     for i in range(a, len(l1)):
#         if l1[i] < l1[a]:
#             a = i
#     return a


# def sel_sort(l1):
#     a = 0
#     for i in range(a, len(l1)):
#         l1[a], l1[find_min(l1)] = l1[find_min(l1)], l1[a]
#         a += 1
#     return l1

# second

# def sel_sort(l1):
#     a = c = 0
#     for i in range(len(l1)):
#         a = i
#         for j in range(c, len(l1)):
#             if l1[j] < l1[a]:
#                 a = j
#         l1[a], l1[c] = l1[c], l1[a]
#         c += 1
#     return l1

# third

def sel_sort(l1):
    for i in range(len(l1)):
        t = l1[i]
        for k in range(i, -1, -1):
            if k > 0 and ls[k - 1] > t:
                l1[k] = l1[k - 1]
            else:
                l1[k] = t
                break
    return l1


ls = [2, 8, 5, 3, 9, 4, 1]
print(sel_sort(ls))
