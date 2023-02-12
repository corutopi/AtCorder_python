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
def solve(N, A, B):
    # 1 と 0 は同じ部
    dp = [A[1] + A[0] + B[0], A[0]]
    for i in range(2, N):
        if i != N - 1:
            same0 = min(dp[0] + B[i - 1] + A[i], dp[1] + A[i])
            diff0 = min(dp[0], dp[1] + B[i - 1])
        else:
            same0 = min(dp[0] + B[i - 1] + A[i], dp[1] + A[i]) + B[-1]
            diff0 = min(dp[0], dp[1] + B[i - 1])
        dp = [same0, diff0]
    ans = min(dp)

    # 1 と 0 は違う部
    dp = [A[1], B[0]]
    for i in range(2, N):
        if i != N - 1:
            same0 = min(dp[0] + B[i - 1] + A[i], dp[1] + A[i])
            diff0 = min(dp[0], dp[1] + B[i - 1])
        else:
            same0 = min(dp[0] + B[i - 1] + A[i], dp[1] + A[i])
            diff0 = min(dp[0], dp[1] + B[i - 1]) + B[-1]
        dp = [same0, diff0]
    ans = min(min(dp), ans)

    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(N, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
