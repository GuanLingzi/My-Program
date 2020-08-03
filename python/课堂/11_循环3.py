n = 9
for row in range(1, n + 1):
    for col in range(1, row + 1):
        print(f'{col} * {row} = {col * row}  ', end='')
    print()
