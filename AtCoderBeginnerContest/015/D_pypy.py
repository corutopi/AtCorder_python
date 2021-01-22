"""
解説を参考に改良
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(W, N, K, AB):
    dp = [[0] * (W + 1) for _ in range(K + 1)]  # use num, width
    new = [[0] * (W + 1) for _ in range(K + 1)]
    for i in range(N):
        a, b = AB[i]
        for k in range(1, K + 1):
            for w in range(1, W + 1):
                if w < a:
                    new[k][w] = dp[k][w]
                    continue
                new[k][w] = max(dp[k][w], dp[k - 1][w - a] + b)
        dp, new = new, dp
    print(dp[K][W])


if __name__ == '__main__':
    W = int(input())
    N, K = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(W, N, K, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # W = 10000
    # N, K = 50, 50
    # AB = [[randint(1, 100), randint(1, 100)] for _ in range(N)]
    # solve(W, N, K, AB)
