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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    if N == 2:
        print(min(A))
        return
    dp = [inf] * N
    dp[0] = A[0]
    dp[1] = A[0]
    for i in range(2, N):
        dp[i] = min(dp[i - 2] + A[i - 1], dp[i - 1] + A[i - 1])
    ans1 = dp[-1]
    dp = [inf] * N
    dp[0] = A[-1]
    dp[1] = dp[0] + A[0]
    for i in range(2, N):
        if i == N - 1:
            dp[i] = min(dp[i - 2] + A[i - 1], dp[i - 1])
        else:
            dp[i] = min(dp[i - 2] + A[i - 1], dp[i - 1] + A[i - 1])
    ans2 = dp[-1]
    print(min(ans1, ans2))


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
