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
def solve(N, A, x):
    dp = [0] * 5001
    dp[2500] = 1
    y = [xi - A for xi in x]
    for yi in y:
        new_dp = [0] * 5001
        for i in range(5001):
            new_dp[i] += dp[i]
            new_dp[i] += dp[i - yi] if 0 <= i - yi < 5001 else 0
        dp = new_dp
    print(dp[2500] - 1)


if __name__ == '__main__':
    N, A = map(int, input().split())
    x = [int(i) for i in input().split()]
    solve(N, A, x)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 50
    # A = 50
    # x = [50] * N
    # solve(N, A, x)
