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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, X, Y):
    X.sort()
    Y.sort()
    sum_x = sum(((2 * n - N - 1) * X[n - 1]) % mod for n in range(1, N + 1))
    sum_y = sum(((2 * m - M - 1) * Y[m - 1]) % mod for m in range(1, M + 1))

    print((sum_x * sum_y) % mod)


if __name__ == '__main__':
    N, M = map(int, input().split())
    X = [int(i) for i in input().split()]
    Y = [int(i) for i in input().split()]
    solve(N, M, X, Y)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
