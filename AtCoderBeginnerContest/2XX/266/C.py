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


def angle(ax, ay, bx, by, cx, cy):
    import math

    m1, m2 = bx - ax, by - ay
    n1, n2 = cx - ax, cy - ay
    cos = (m1 * n1 + m2 * n2) / ((m1 ** 2 + m2 ** 2) ** 0.5 *
                                 (n1 ** 2 + n2 ** 2) ** 0.5)
    return math.degrees(math.acos(cos))


# from decorator import stop_watch
#
#
# @stop_watch
def solve(A1, A2, B1, B2, C1, C2, D1, D2):
    h = angle(B1, B2, A1, A2, C1, C2)
    i = angle(C1, C2, B1, B2, D1, D2)
    j = angle(D1, D2, C1, C2, A1, A2)
    k = angle(A1, A2, D1, D2, B1, B2)
    # print(h, i, j, k)
    print('Yes' if abs(360 - sum([h, i, j, k])) < EPS else 'No')


if __name__ == '__main__':
    A1, A2 = map(int, input().split())
    B1, B2 = map(int, input().split())
    C1, C2 = map(int, input().split())
    D1, D2 = map(int, input().split())
    solve(A1, A2, B1, B2, C1, C2, D1, D2)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
