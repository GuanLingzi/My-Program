n = int(input("Please input a integer number:"))
h = n // 3600
m = n // 60 % 60
s = n % 60
print(f'{h:02}:{m:02}:{s:02}')
