ls = [1, 2, 3, 4, 5, 6]
ls[0] = 'b'
print(ls)

tup = 1, 2, 3, 4, 5
print(tup[0])

a = 1
b = 2
# c = b, a
# print(c)
# print(type(c))
# a, b = c
# print(a, b)
a, b = b, a + b
print(a, b)
a, b = b, a + b
print(a, b)

tup1 = 1,
print(type(tup1))

liu = ("liu", 100, 1.4, 59)
tan = ("tan", 99, 1.6, 100)
guan = ("guan", 80, 1.9, 12)

banji = [liu, tan, guan]

for name in banji:
    print(f"""
name:{name[0]}
weight:{name[1]}
height:{name[2]}
python:{name[3]}
""")

a = "1"
b = 2
c = 3
d = 4
ls = [c]
print(id(ls))
tup_ls = (a, b, ls)
print("tup_ls[0]", id(tup_ls[0]))
print("a", id(a))
a = 1111
print("a", id(a))
print("tup_ls[0]", id(tup_ls[0]))

print(tup_ls)
ls[0] = d
print("ls", id(ls))

print(tup_ls)

# 斐波那契数列
Fa = 0
Fb = 1
Fc = 1
while Fc <= 100:
    print(Fc)
    Fc = Fa + Fb
    Fa, Fb = Fb, Fc
