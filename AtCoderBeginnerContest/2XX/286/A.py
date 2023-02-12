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
def solve(N, P, Q, R, S, A):
    P -= 1
    Q -= 1
    R -= 1
    S -= 1
    for i in range(Q - P + 1):
        A[P + i], A[R + i] = A[R + i], A[P + i]
    print(*A)


if __name__ == '__main__':
    N, P, Q, R, S = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, P, Q, R, S, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
