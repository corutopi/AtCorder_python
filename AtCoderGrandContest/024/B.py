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
def solve(N, P):
    dp = [0] * (N + 1)
    for p in P:
        dp[p] = dp[p - 1] + 1
    print(N - max(dp))


if __name__ == '__main__':
    N = int(input())
    P = [int(input()) for _ in range(N)]
    solve(N, P)

    # # test
    # from random import randint, shuffle
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2 * 10 ** 5
    # P = [i + 1 for i in range(N)]
    # shuffle(P)
    # solve(N, P)
