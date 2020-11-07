import random
xiaoming = {"name": "小明",
            "age": 18,
            "gender": True,
            "height": 1.75}

print(xiaoming)

d1 = {"name": "yaoming",
      "age": 18,
      "gender": "nv",
      "height": 2.3,
      "hobby": "basketball"}

for value in d1.values():
    print(value)

for item in d1.items():
    print(f'{item[0]:8} : {item[1]}')

num = []
for i in range(1000):
    num.append(random.randint(20, 100))
    num.sort()
print(num)
for j in num:
    print(len(num[j]))
