"""
解説を参考に作成
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M):
    # # 全部の項を1つずつ変換した場合の総コスト
    # cost_all = N * pow(M, N, mod2)
    # for n in range(1, N):
    #     nn = N - n  # 解説の文字で言うと i - j = n となる組み合わせの個数を表す
    #     sum_ij = 0
    #     for x in range(1, M + 1):
    #         # i, j を固定した場合に, i, j を同時に解決できる(コストが1減る)組み合わせ数を計算している.
    #         # Ai == Aj == x の場合に, i < k < j となるすべての Ak は > x でなくてはならない.
    #         # Ak >= x としないのは, Ai == Ak  となるような場合の数え上げを別でしているので、その重複をなくすため.
    #         sum_ij += pow(M - x, n - 1, mod2)
    #     # i, j 間以外の値は何でもよいので M ** (N - (i - j) - 1 = N - n - 1) を乗算する
    #     # これを各 i, j 毎に行うと N * (N - 1) * M になってしまう.
    #     # そこで i - j が同じであれば計算結果も同じになることを利用し, i - j = n となる組み合わせ数(nn)を乗算する.
    #     # 計算結果が総コスト数から削減可能な値となるので減算する.
    #     cost_all -= (sum_ij * pow(M, N - n - 1, mod2) * nn) % mod2
    # print(cost_all % mod2)
    # # ただこれだとpypyでも4秒かかるのでpowを前計算するなどしなくてはならない.

    cost_all = N * pow(M, N, mod2)
    pow_M_mod2 = [1, M]
    for _ in range(N):
        pow_M_mod2.append((pow_M_mod2[-1] * M) % mod2)
    pow_Mx_n1 = [[1] for _ in range(M + 1)]
    for m in range(M + 1):
        for _ in range(N + 1):
            pow_Mx_n1[m].append((pow_Mx_n1[m][-1] * m) % mod2)
    for n in range(1, N):
        nn = N - n
        sum_ij = 0
        for x in range(1, M + 1):
            sum_ij += pow_Mx_n1[M - x][n - 1]
        cost_all -= (sum_ij * pow_M_mod2[N - n - 1] * nn) % mod2
    print(cost_all % mod2)


if __name__ == '__main__':
    N, M = map(int, input().split())
    solve(N, M)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N, M = 5000, 5000
    # solve(N, M)
