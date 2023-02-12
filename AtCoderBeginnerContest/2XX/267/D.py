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
def solve(N, M, A):
    dp = [0] * (N + 1)
    dp_new = [0] * (N + 1)
    for i in range(1, M + 1):
        for j in range(N + 1):
            if j < i:
                dp_new[j] = 0
            elif j == i:
                dp_new[j] = dp[j - 1] + A[j - 1] * i
            else:
                dp_new[j] = max(dp_new[j - 1], dp[j - 1] + A[j - 1] * i)
        dp, dp_new = dp_new, dp
    print(max(dp[M:]))


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, M, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
