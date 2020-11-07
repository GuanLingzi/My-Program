d = {"张三": 97, "李四": 59, "王五": 100}

print(sorted(d.items(), key=lambda x: x[1], reverse=True))

print("\"hello guido's\'s python\"")
print("%s\t%s" % ("hello", "world"))

chaichixiang = "柴智翔是废柴翔"
i = 0
print(chaichixiang[2])
for c in chaichixiang:
    print(chaichixiang[i])
    i = i + 1

f = "hello hello"
print(len(f))
a = "h"
print(f.count(a))
print(f.index(a))
