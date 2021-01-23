money = 0


def dream(money):
    money = 100000000
    print(f"我有{money}元人民币了！")
    return "醒醒，该上课了^_^"


mama = dream(money)
print(mama)
print(f"你其实有{money}元人民币")


def pao_ying_bi(do: str) -> str:
    import random
    flag = random.choice([0, 1])
    if flag:
        return "正面...这次不算，重抛一次"
    else:
        return f"反面！天意如此，不用{do}了！"


print(pao_ying_bi("做作业"))
