"""
解説AC
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, D):
    dp = [[[-1] * D for _ in range(K + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 0
    for i, j, k in ((i, j, k)
                    for i in range(N)
                    for j in range(K + 1)
                    for k in range(D)):
        if dp[i][j][k] == -1: continue
        dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
        if j != K:
            dp[i + 1][j + 1][(k + A[i]) % D] = max(
                dp[i + 1][j + 1][(k + A[i]) % D], dp[i][j][k] + A[i])
    print(dp[N][K][0])


if __name__ == '__main__':
    N, K, D = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, K, D)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
