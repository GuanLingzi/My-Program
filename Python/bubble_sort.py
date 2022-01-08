def bubble_sort(n):
    for k in range(len(n) - 1):
        for i in range(len(n) - 1):
            if n[i] > n[i + 1]:
                n[i], n[i + 1] = n[i + 1], n[i]
            else:
                continue
    return n


ls = [2, 5, 3, 7, 1, 3]
print(bubble_sort(ls))
