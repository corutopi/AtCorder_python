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
def solve(N, AB):
    dp = [1, 1]
    for i in range(1, N):
        dp = [
            (dp[0] if AB[i][0] != AB[i - 1][0] else 0) +
            (dp[1] if AB[i][0] != AB[i - 1][1] else 0),
            (dp[0] if AB[i][1] != AB[i - 1][0] else 0) +
            (dp[1] if AB[i][1] != AB[i - 1][1] else 0)]
        dp = [dp[0] % mod2, dp[1] % mod2]
    print(sum(dp) % mod2)


if __name__ == '__main__':
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
