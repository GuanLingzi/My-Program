B = int(input())
In_1 = int(input(), B)
In_2 = int(input(), B)

Ans = In_1 + In_2

s = ""

while Ans != 0:
    a = Ans % B
    if a <= 9:
        s += str(a)
    else:
        s += chr(a + 55)
    Ans //= B

s = s[::-1]

print(s)
