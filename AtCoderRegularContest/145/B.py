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
def solve(N, A, B):
    ans = 0
    if A <= B:
        if N < A:
            ans = 0
        else:
            ans = N - (A - 1)
    else:
        d, m = divmod(N, A)
        if d == 0:
            ans = 0
        else:
            ans = (d - 1) * B + 1 + min(m, B - 1)
    print(ans)


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    solve(N, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
