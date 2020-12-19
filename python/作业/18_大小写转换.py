s = input("Please input a string(Only English):")
list1 = []
i = 0
for j in s:
    if i % 2 == 0:
        j = j.upper()
        list1.append(j)
        i += 1
    else:
        j = j.lower()
        list1.append(j)
        i += 1
print("".join(list1))
