# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, TXA):
    hole = 5 + 2
    point = [[0] * hole for _ in range(10 ** 5 + 1)]
    for t, x, a in TXA:
        point[t][x + 1] += a

    dp = [-inf] * hole
    dp[1] = point[0][1]
    for p in range(1, 10 ** 5 + 1):
        dp_new = [-inf] * hole
        for i in range(1, hole - 1):
            dp_new[i] = max(dp[i - 1:i + 2]) + point[p][i]
        dp = dp_new
    print(max(dp))


if __name__ == '__main__':
    N = int(input())
    TXA = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, TXA)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
