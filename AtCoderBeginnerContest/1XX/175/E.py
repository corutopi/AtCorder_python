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
def solve(R, C, K, rcv):
    mass = [[0] * (C + 1) for _ in range(R + 1)]
    for r, c, v in rcv:
        mass[r][c] = v
    dp = [[0] * 4 for _ in range(C + 1)]
    for r in range(1, R + 1):
        new_dp = [[0] * 4 for _ in range(C + 1)]
        for c in range(1, C + 1):
            m = max(dp[c])
            new_dp[c][0] = max(m, new_dp[c - 1][0])
            new_dp[c][1] = max(m + mass[r][c], new_dp[c - 1][0] + mass[r][c],
                               new_dp[c - 1][1])
            new_dp[c][2] = max(new_dp[c - 1][1] + mass[r][c],
                               new_dp[c - 1][2])
            new_dp[c][3] = max(new_dp[c - 1][2] + mass[r][c],
                               new_dp[c - 1][3])
        dp = new_dp
    print(max(dp[-1]))


if __name__ == '__main__':
    R, C, K = map(int, input().split())
    rcv = [[int(i) for i in input().split()] for _ in range(K)]
    solve(R, C, K, rcv)

    # # test
    # from random import randint
    # import string
    # # import tool.testcase as tt
    # # from tool.testcase import random_str, random_ints
    #
    # R, C = 3000, 3000
    # K = 2 * 10 ** 5
    # rcv = [[randint(1, R), randint(1, C), randint(1, 10 ** 9)] for _ in
    #        range(K)]
    # solve(R, C, K, rcv)
