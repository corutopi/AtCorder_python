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
def solve(N, X, AB):
    dp = [1] + [0] * 10000
    for a, b in AB:
        new_dp = [0] * 10001
        for i in range(10001):
            if dp[i] == 0: continue
            if i + a < 10001:
                new_dp[i + a] = 1
            if i + b < 10001:
                new_dp[i + b] = 1
        dp = new_dp
    print('Yes' if dp[X] == 1 else 'No')


if __name__ == '__main__':
    N, X = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, X, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
