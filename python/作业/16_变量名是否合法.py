res = True
Value = input('please input value name:')
if Value[0].isdigit():
    res = False
else:
    for i in Value:
        if i.isalnum() or i == '_':
            res = True
        else:
            res = False
            break
print(res)
