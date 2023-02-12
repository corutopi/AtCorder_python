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


def area_triangle_octuple(x1, y1, x2, y2, x3, y3):
    """座標(x1, y1), (x2, y2), (x3, y3) で表される三角形の面積.
    """
    # a = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** d0_5
    # b = (abs(x2 - x3) ** 2 + abs(y2 - y3) ** 2) ** d0_5
    # c = (abs(x3 - x1) ** 2 + abs(y3 - y1) ** 2) ** d0_5
    # s = (a + b + c) / 2
    # return (s * (s - a) * (s - b) * (s - c)) ** d0_5
    return 4 * abs((x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3))


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, XY):
    S = 0
    for i in range(1, N - 1):
        S += area_triangle_octuple(*XY[0], *XY[i], *XY[i + 1])
    a = S // 4

    ans = S
    q = 1
    E = 0
    for p in range(N):
        while True:
            x = area_triangle_octuple(*XY[p], *XY[q], * XY[(q + 1) % N])
            ans = min(ans, abs(a - (E + x)))
            if E + x > a:
                break
            E += x
            q += 1
            q %= N
        E -= area_triangle_octuple(*XY[p], *XY[(p + 1) % N], *XY[q])
    print(ans)


if __name__ == '__main__':
    N = int(input())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, XY)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
