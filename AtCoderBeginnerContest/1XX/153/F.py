# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, D, A, XH):
    XH.sort()
    bom_rch = [0]  # iを左端として爆発させた時に爆弾の届かない最初のモンスター
    bom_num = [0]  # iを左端として爆発させた数
    j = 0
    for i in range(N):
        x = XH[i][0]
        while j < N and XH[j][0] <= x + D * 2:
            j += 1
        bom_rch.append(j)

    left_bom_point = 0
    bom = 0
    for i in range(N):
        x, h = XH[i]
        while bom_rch[left_bom_point] <= i:
            bom -= bom_num[left_bom_point]
            left_bom_point += 1
        now_bom = max(ceil((h - A * bom) / A), 0)
        bom_num.append(now_bom)
        bom += now_bom

    print(sum(bom_num))


if __name__ == '__main__':
    N, D, A = map(int, input().split())
    XH = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, D, A, XH)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
