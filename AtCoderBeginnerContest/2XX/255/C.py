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
def solve(X, A, D, N):
    if D == 0:
        print(abs(A - X))
    elif D > 0 and A <= X <= A + (D * (N - 1)):
        x = X - A
        y = x // D
        print(min(abs(A + D * y - X), abs(A + D * (y + 1) - X)))
    elif D < 0 and A + (D * (N - 1)) <= X <= A:
        x = X - A
        y = x // D
        print(min(abs(A + D * y - X), abs(A + D * (y + 1) - X)))
    else:
        print(min(abs(A - X), abs(A + (D * (N - 1) - X))))


if __name__ == '__main__':
    X, A, D, N = map(int, input().split())
    solve(X, A, D, N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
