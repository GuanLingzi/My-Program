"""
综合测试三
一共 8 题，每题 100 分。
"""

# todo: 注意：
#  1. 考试时间100分钟，注意时间分配。
#  2. 所有题目程序运行时间限制为1000ms, 调试时请自行计时。
#  3. 输入输出注意格式要求, 不要输出无关代码。

"""
*************************以下为示范题目************************
0.示例代码：a + b
给你两个数a、b，请你计算它们的和，并输出。
示例：
输入：3 2
输出：5
*************************以下为示范解答***************************
解答：
s = input().split()
res = int(s[0]) + int(s[1])
print(res)
# *************************以下为正式考题***************************
"""

"""
1.输入一个整数n, 返回n以内的素数个数. (2 <= n <= 1e6)
示例：
输入：100
输出：25
"""


def primes(a1):
    bls = [0, 1] * (a1 // 2 + 1)
    bls[1], bls[2] = 0, 1
    p_l = []

    for index in range(3, int(a1 ** 0.5) + 1):
        if bls[index]:
            for i1 in range(index * index, a1, index * 2):
                bls[i1] = 0
    for i1 in range(a1):
        if bls[i1]:
            p_l.append(i1)
    return len(p_l)


n = int(input())
print(primes(n))
"""
2.输入 1 个整数 n 表示进制(2 <= n <= 36); 每行一个 n 进制数正整数。数字的每一位属于{0，1，2，...8，9，A，B...}; 
  以及 1 个字符 op 表示操作符, 输出 4 进制下该运算的结果。
  说明:  1.op 仅包含 +-*/
        2.保证结果大于 0
        3.保证能整除所以不要有小数. 如果除数为零应输出 ERR
示例：
输入：4
     123
     321
     +
输出：1110
"""


def n_to_ten(in1, in2):
    out1 = int(in1)
    out2 = int(in2)
    return out1, out2


n = int(input())
in_1 = input()
in_2 = input()
op = input()

print(n_to_ten(in_1, in_2))
"""
3.求 a 和 b 的最大公约数和最小公倍数. 1 <= a, b <= 1e9. (1e9 即 1000000000)
示例：
输入：8 20
输出：4 40
"""


def ys(x, z):
    l3 = []
    for ans in range(1, min(x, z) + 1):
        if x % ans == 0 and z % ans == 0:
            l3.append(ans)
    l3.sort()
    return l3[-1]


def bs(x, z):
    for ans in range(max(x, z), x * z + 1):
        if ans % x == 0 and ans % z == 0:
            return ans


a, b = map(int, input().split())
print(ys(a, b), bs(a, b))
"""
4. 给定一个序列 a, 当且仅当 i < j 且 a[i] > a[j] 时, 我们称二元组 (i, j) 为一个逆序对。
   现在给出a序列，问逆序对总共有多少个。 (提示: 排序)

示例：
输入：4 1 3 2 1
输出：7
"""


def judge(a1):
    sum1 = 0
    for o in range(0, len(a1)):
        for p in range(0, len(a1)):
            if o < p and a1[o] > a1[p]:
                sum1 += 1
    return sum1


a = list(map(int, input().split()))

print(judge(a))
"""
5. (接上题)当且仅当a[i1] ≠ a[i2] 或 a[j1] ≠ a[j2] 时, 我们称两个逆序对 (i1, j1), (i2, j2)本质不同。
   现在给出a序列，问本质不同逆序对个数。 (提示: 集合)

示例：
输入：4 1 3 2 1
输出：6
"""


def cre_l(a1):
    ls1 = []
    l2 = []
    for m1 in range(0, len(a1)):
        for n1 in range(0, len(a1)):
            if m1 < n1 and a1[m1] > a1[n1]:
                l2.append(m1)
                l2.append(n1)
                ls1.append(l2)
                l2 = []
    return ls1


def judge(a1):
    sum3 = 0
    for n2 in range(0, len(a1) - 1):
        if a1[n2][0] != a1[n2 + 1][0] or a1[n2][1] != a1[n2 + 1][1]:
            sum3 += 1
    return sum3


a = input().split(" ")

print(judge(cre_l(a)))
"""
6.输入一个数 n 和一个整数列表 ls, 输出 n 是否在 ls 中, 在的话输出 True, 否则输出 False. ls 中有至多 1e8 个元素.
示例：
输入：8
     1 3 7 8
输出：True
"""
n3 = int(input())
ls = input().split(" ")
print(str(n3) in ls)
"""
7. 输入 2 个整数 m 和 n, 表示 m 行 n 列个数, 以及一个矩形(长宽均从 1 开始)的左上角的坐标 x1, y1 和右下角的坐标 x2, y2, 输出该矩形内所有数的和.
示例：
输入：3 3
     1 2 3
     4 5 6
     7 8 9
     2 2
     3 3
输出：28
"""
m, n5 = map(int, input().split())
"""
8.楼梯有 N 阶, N <= 20，上楼可以一步上一阶，也可以一步上二阶。
  编一个程序，计算共有多少种不同的走法。(提示: 递归)
示例：
输入：6
输出：13
"""


def steps(s):
    if s == 1:
        return 1
    elif s == 2:
        return 2
    else:
        return steps(s - 1) + steps(s - 2)


N = int(input())
print(steps(N))
