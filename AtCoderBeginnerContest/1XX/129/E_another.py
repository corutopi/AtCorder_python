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
def solve(S):
    dp = [0, 1]
    for s in S:
        dp = [dp[0] * 3, dp[1]] if s == '0' else [dp[0] * 3 + dp[1], dp[1] * 2]
        dp = [dp[0] % mod, dp[1] % mod]
    print(sum(dp) % mod)


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
