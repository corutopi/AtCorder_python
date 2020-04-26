# 解説を参考に作成
# さらに 提出 #12403542 を参考


def solve():
    S = input()
    lenS = len(S)
    mod_list = [0] * 2019
    x = 0
    for i in range(lenS):
        x = (int(S[lenS - 1 - i]) * pow(10, i, 2019) + x) % 2019
        mod_list[x] += 1

    result = 0
    for i, ml in enumerate(mod_list):
        if i == 0:
            result += ml
        result += int(ml * (ml - 1) / 2)
    print(result)


if __name__ == '__main__':
    solve()
