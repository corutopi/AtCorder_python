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
def solve(N, XC):
    color_lr = [[inf, -inf] for _ in range(N + 1)]
    for x, c in XC:
        color_lr[c][0] = min(color_lr[c][0], x)
        color_lr[c][1] = max(color_lr[c][1], x)
    # 同色のボールの左端を最後に拾う場合の最小値と座標, 右端を最後に拾う場合のry
    dp = [[0, 0], [0, 0]]
    for n in range(N + 1):
        new_dp = [[0, 0], [0, 0]]
        c_left, c_right = color_lr[n]
        if c_left == inf: continue
        # last left
        b_l_cost = dp[0][0] + abs(dp[0][1] - c_right) + abs(c_right - c_left)
        b_r_cost = dp[1][0] + abs(dp[1][1] - c_right) + abs(c_right - c_left)
        new_dp[0] = [b_l_cost, c_left] if b_l_cost < b_r_cost \
            else [b_r_cost, c_left]
        # last right
        b_l_cost = dp[0][0] + abs(dp[0][1] - c_left) + abs(c_left - c_right)
        b_r_cost = dp[1][0] + abs(dp[1][1] - c_left) + abs(c_left - c_right)
        new_dp[1] = [b_l_cost, c_right] if b_l_cost < b_r_cost \
            else [b_r_cost, c_right]
        dp = new_dp
    print(min(dp[0][0] + abs(dp[0][1]), dp[1][0] + abs(dp[1][1])))


if __name__ == '__main__':
    N = int(input())
    XC = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, XC)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
