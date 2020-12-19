n = 8000
h = n // 3600
m = n // 60 - h * 60
s = n % 60
print(h, m, s)
