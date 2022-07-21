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


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, a, b, A):
    def func(x):
        plus = 0
        minus = 0
        for n in A:
            if n > x:
                minus += (n - x) // b
            elif n < x:
                plus += (x - n) // a + (1 if (x - n) % a > 0 else 0)
        return plus <= minus
    print(binary_search(1, 10 ** 9 + 1, func))


if __name__ == '__main__':
    N, a, b = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, a, b, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
