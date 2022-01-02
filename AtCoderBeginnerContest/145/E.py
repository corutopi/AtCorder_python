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
def solve(N, T, AB):
    dp = [0] * (T + 1)
    AB.sort()
    for a, b in AB:
        dx = [0] * (T + 1)
        for i in range(min(T + 1, a)):
            dx[i] = dp[i]
        for i in range(T):
            dx[min(T, i + a)] = max(dp[i] + b, dp[min(T, i + a)])
        dp = dx
    print(dp[-1])


if __name__ == '__main__':
    N, T = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, T, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
