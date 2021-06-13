"""
解説を参考に作成
"""
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
def solve(N, DCS):
    DCS.sort()
    dp = [[0] * 5001 for _ in range(N + 1)]
    dp = [0] * 5001
    for d, c, s in DCS:
        dp_new = [0] * 5001
        for j in range(1, 5001):
            if j < c or d < j:
                dp_new[j] = dp[j]
            else:
                dp_new[j] = max(dp[j], dp[j - c] + s)
        dp = dp_new
    print(max(dp))


if __name__ == '__main__':
    N = int(input())
    DCS = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, DCS)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 5000
    # DCS = [[randint(1, 5000), randint(1, 5000), randint(1, 10 ** 9)] for _ in range(N)]
    # solve(N, DCS)
