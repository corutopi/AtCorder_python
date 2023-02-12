# 解説と以下を参考に作成
#   https://atcoder.jp/contests/abc225/submissions/27056917
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
from decimal import Decimal

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, xy):
    line = []
    for x, y in xy:
        t1 = Decimal(y) / Decimal(x - 1) if x > 1 else float('inf')
        t2 = Decimal(y - 1) / Decimal(x)
        line.append([t1, t2])
    line.sort()

    ans = 0
    b = -1
    for x, y in line:
        if y >= b:
            ans += 1
            b = x
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    xy = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(N, xy)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
