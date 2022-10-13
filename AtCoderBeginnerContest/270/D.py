import sys
sys.setrecursionlimit(10 ** 6)
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
def solve(N, K, A):
    A.reverse()
    TAKAHASHI, AOKI = 0, 1
    dp = [[0, 0]] + [[-1, -1] for _ in range(N)]

    def memo(storn_num, player):
        if player == TAKAHASHI:
            aite = AOKI
            result = -1
        else:
            aite = TAKAHASHI
            result = inf

        for a in A:
            if storn_num < a: continue
            if dp[storn_num - a][aite] == -1:
                memo(storn_num - a, aite)

            if player == TAKAHASHI:
                result = max(result, dp[storn_num - a][aite] + a)
            else:
                result = min(result, dp[storn_num - a][aite])

        dp[storn_num][player] = result

    memo(N, TAKAHASHI)

    print(dp[-1][0])


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
