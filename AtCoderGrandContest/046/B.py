# 解説AC
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
def solve(A, B, C, D):
    dp = [[0, 0] for _ in range(C - A + 1)]
    dp[0][0] = 1
    for i in range(1, len(dp)):
        dp[i][0] = dp[i - 1][0] * B
        dp[i][0] %= mod2
    for b in range(1, D - B + 1):
        new_dp = [[0, 0] for _ in range(C - A + 1)]
        new_dp[0][0] = (dp[0][0] * A) % mod2

        for a in range(1, C - A + 1):
            new_dp[a][0] = sum(new_dp[a - 1]) * (B + b)
            new_dp[a][0] %= mod2
            new_dp[a][1] = dp[a][0] + dp[a][1] * (A + a)
            new_dp[a][1] %= mod2
        dp = new_dp
    print(sum(dp[-1]) % mod2)


if __name__ == '__main__':
    A, B, C, D = map(int, input().split())
    solve(A, B, C, D)
    # solve(1,1,3000,3000)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
