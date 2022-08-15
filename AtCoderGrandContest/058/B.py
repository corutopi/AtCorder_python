"""
解説見た
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
def solve(N, P):
    # make L, R
    stack = []
    L = []
    for i in range(N):
        while stack:
            if P[stack[-1]] > P[i]: break
            stack.pop()
        L.append(-1 if len(stack) == 0 else stack[-1])
        stack.append(i)
    stack = []
    R = []
    for i in range(N - 1, -1 , -1):
        while stack:
            if P[stack[-1]] > P[i]: break
            stack.pop()
        R.append(N if len(stack) == 0 else stack[-1])
        stack.append(i)
    R.reverse()

    # dp
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(N):
        new_dp = [1]
        for j in range(1, N + 1):
            tmp = 0
            if L[i] < j - 1 and j <= R[i]:
                tmp += new_dp[-1]
            tmp += dp[j]
            new_dp.append(tmp % mod2)
        dp = new_dp
    print(dp[-1])


if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]
    solve(N, P)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
