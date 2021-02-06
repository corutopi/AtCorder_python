"""
解説と以下などを参考に作成
    https://atcoder.jp/contests/abc191/submissions/20013035
"""
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
def solve(X, Y, R):
    ans = 0
    for i in range(ceil(X - R), floor(X + R) + 1):
        if R - abs(X - i) < 0:
            continue
        y = Decimal(R ** 2 - (X - i) ** 2).sqrt()
        ans += floor(Y + y + 1) - ceil(Y - y - 1) - 1
    print(ans)


if __name__ == '__main__':
    X, Y, R = map(Decimal, input().split())
    solve(X, Y, R)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
