# 解説と 13355391 を参考に実装予定


import math


def solve():
    N = int(input())
    ABs = [[int(i) for i in input().split()] for _ in range(N)]
    mod = 10 ** 9 + 7

    lonlieness = 0
    pairs = {}
    for AB in ABs:
        a, b = AB
        if a == 0 and b == 0:
            lonlieness += 1
            continue
        elif a == 0:
            a, b = -1, 0
            bad_a, bad_b = 0, 1
        elif b == 0:
            a, b = (0, 1)
            bad_a, bad_b = -1, 0
        else:
            _gcd = math.gcd(a, b)
            a //= _gcd
            b //= _gcd
            bad_a = -b
            bad_b = a
            if b < 0:
                a, b = -a, -b
            if bad_b < 0:
                bad_a, bad_b = -bad_a, -bad_b
        pairs.setdefault((a, b), 0)
        pairs.setdefault((bad_a, bad_b), 0)  # 仲の悪いグループも登録しておく
        pairs[(a, b)] += 1

    permutations = []
    for i, pair in enumerate(pairs.keys()):
        if i % 2 == 1:
            continue  # 仲の悪いグループは隣り合っているので飛び石で計算
        a, b = pair
        bad_a, bad_b = -b, a
        if bad_b < 0:
            bad_a, bad_b = -bad_a, -bad_b
        # gourp1 から1匹以上選ぶパターン + group2 から1匹以上選ぶパターン + どちらからも選ばないパターン計算する.
        # group1 と group2 は仲が悪いので同時に選ばれることはない.
        group_num = pow(2, pairs[(a, b)], mod) - 1
        badgroup_num = pow(2, pairs[(bad_a, bad_b)], mod) - 1
        permutations.append(group_num + badgroup_num + 1)

    result = 1
    for p in permutations:
        result = result * p % mod

    # 全員と仲が悪いイワシのパターンを足し, すべてのイワシを選ばないパターンを除外.
    result = (result + lonlieness - 1) % mod
    print(result)


if __name__ == '__main__':
    solve()
