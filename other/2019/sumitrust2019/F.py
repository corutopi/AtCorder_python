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
def solve(T1, T2, A1, A2, B1, B2):
    if (A1 > B1 and A1 * T1 + A2 * T2 > B1 * T1 + B2 * T2) or \
            (A1 < B1 and A1 * T1 + A2 * T2 < B1 * T1 + B2 * T2):
        print(0)
        return
    if A1 * T1 + A2 * T2 == B1 * T1 + B2 * T2:
        print('infinity')
        return
    X = abs(A1 * T1 - B1 * T1)
    Y = abs((A1 * T1 + A2 * T2) - (B1 * T1 + B2 * T2))
    print(X // Y + ceil(X / Y))


if __name__ == '__main__':
    T1, T2 = map(int, input().split())
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    solve(T1, T2, A1, A2, B1, B2)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
