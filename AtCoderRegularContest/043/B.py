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
def solve(N, D):
    D.sort()
    dp = [[1] + [0] * 4 for _ in range(D[-1] + 1)]
    task = [0] * (D[-1] + 1)
    for d in D:
        task[d] += 1
    for i in range(1, len(dp)):
        for j in range(1, 5):
            dp[i][j] = dp[i - 1][j] + dp[i // 2][j - 1] * task[i]
            dp[i][j] %= mod
    print(dp[-1][-1])


if __name__ == '__main__':
    N = int(input())
    D = [int(input()) for _ in range(N)]
    solve(N, D)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
