a = input()
b = int(input())
for i in range(len(a)):
    if ord(a[i])+3 <= 90:
        print(''.join(chr(ord(a[i])+3)))
    elif ord(a[i])+3 <= 122:
        if ord(a[i]) > 96:
            print(''.join(chr(ord(a[i])+3)))
        elif ord(a[i])+3 > 90:
            print(''.join(chr(96+((ord(a[i])+3)-90))))
    else:
        print(''.join(chr(64+((ord(a[i])+3)-122))))
