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

    def memo(stone_num, player):
        if player == TAKAHASHI:
            opponent = AOKI
            result = -1
        else:
            opponent = TAKAHASHI
            result = inf

        for a in A:
            if stone_num < a: continue
            if dp[stone_num - a][opponent] == -1:
                memo(stone_num - a, opponent)

            if player == TAKAHASHI:
                result = max(result, dp[stone_num - a][opponent] + a)
            else:
                result = min(result, dp[stone_num - a][opponent])

        dp[stone_num][player] = result

    memo(N, TAKAHASHI)

    print(dp[N][TAKAHASHI])


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
