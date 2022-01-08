def position(k, ls):  # 读取坐标（索引）
    for i in range(0, len(ls)):
        for j in range(0, len(ls)):
            if ls[i][j] == k:
                return i, j


def judge(ls):  # 判断位置
    for k in range(2, N * N + 1):
        x, y = position(k - 1, ls)
        if x == 0 and y != N - 1:
            ls[- 1][y + 1] = k
        elif x != 0 and y == N - 1:
            ls[x - 1][0] = k
        elif x == 0 and y == N - 1:
            ls[x + 1][y] = k
        elif x != 0 and y != N - 1:
            if ls[x - 1][y + 1] == 0:
                ls[x - 1][y + 1] = k
            else:
                ls[x + 1][y] = k
    return ls


N = int(input())
ls = [[0 for i in range(N)] for k in range(N)]  # 列表初始化
ls[0][N // 2] = 1
ls = judge(ls)

for n in ls:  # 输出
    print(*n)
