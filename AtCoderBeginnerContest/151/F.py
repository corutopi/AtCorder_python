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

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7


def liner_cross_point(a1, b1, c1, a2, b2, c2):
    """return x, y of cross two line 'a1x + b1y + c1 = 0' and 'a2x + b2y + c2 = 0'.

    :param a1:
    :param b1:
    :param c1:
    :param a2:
    :param b2:
    :param c2:
    :return:
    """
    if a1 == 0 or a2 == 0:
        if a2 == 0:
            a1, b1, c1, a2, b2, c2 = a2, b2, c2, a1, b1, c1
        y = - c1 / b1
        x = - (b2 * y + c2) / a2
    elif b1 == 0 or b2 == 0:
        if b2 == 0:
            a1, b1, c1, a2, b2, c2 = a2, b2, c2, a1, b1, c1
        x = - c1 / a1
        y = - (a2 * x + c2) / b2
    else:
        a1, b1, c1 = a1 / b1, b1 / b1, c1 / b1
        a2, b2, c2 = a2 / b2, b2 / b2, c2 / b2
        x = - (c1 - c2) / (a1 - a2)
        y = - a1 * x - c1
    return x, y


def liner_function_integer(x1, y1, x2, y2):
    """return a, b, c of ax + by + c = 0.
    a, b and c are relatively prime integers. a >= 0.
    x1 != x2 or y1 != y2
    :param x1: meet y1 = ax1 + b
    :param y1:
    :param x2: meet y2 = ax2 + b
    :param y2:
    :return:
    """

    def gcd(a, b):
        """最大公約数"""
        a, b = (a, b) if a >= b else (b, a)
        if b == 0:
            return a
        return gcd(b, a % b)

    if x1 == x2:
        # y軸に平行な直線の場合
        a = 1
        b = 0
        c = - x1
    elif y1 == y2:
        # x軸に平行な直線の場合
        a = 0
        b = 1
        c = - y1
    else:
        b = 1 * (x1 - x2)
        a = - (y1 - y2)
        c = - a * x1 - b * y1
        g = gcd(gcd(abs(a), abs(b)), abs(c))
        b //= g
        a //= g
        c //= g
        code = 1 if a > 0 else -1
        b *= code
        a *= code
        c *= code
    return a, b, c


def vertical_line(a, b, c, x, y):
    """retrun a1, b1, c1 of 'a1x + b1y + c = 0' intersect 'ax + by + c = 0' vertically.

    直線A(ax + by + c = 0)上の座標(x, y)を通り,
    直線Aに対して垂直な直線B(a1x + b1x + c1 = 0)を表す a1, b1, c1 を返す.

    :param a:
    :param b:
    :param c:
    :param x:
    :param y:
    :return:
    """
    if a == 0:
        a1 = 1
        b1 = 0
        c1 = - x
    elif b == 0:
        a1 = 0
        b1 = 1
        c1 = - y
    else:
        a, b, c = a / b, b / b, c / b
        b1 = 1
        a1 = -  1 / a
        c1 = - (a1 * x) - (b1 * y)
    return a1, b1, c1


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, XY):
    ans = inf
    for (i, j, k) in ((i, j, k)
                      for i in range(N)
                      for j in range(i + 1, N)
                      for k in range(j + 1, N)):
        a, b, c = liner_function_integer(*XY[i], *XY[j])
        if a * XY[k][0] + b * XY[k][1] + c == 0:
            continue

        p, q = liner_cross_point(
            *vertical_line(*liner_function_integer(*XY[i], *XY[j]),
                           (XY[i][0] + XY[j][0]) / 2,
                           (XY[i][1] + XY[j][1]) / 2),
            *vertical_line(*liner_function_integer(*XY[i], *XY[k]),
                           (XY[i][0] + XY[k][0]) / 2,
                           (XY[i][1] + XY[k][1]) / 2),
        )
        r2 = abs(XY[i][0] - p) ** 2 + abs(XY[i][1] - q) ** 2
        for l in range(N):
            x, y = XY[l]
            if r2 < abs(x - p) ** 2 + abs(y - q) ** 2 - EPS:
                break
        else:
            ans = min(ans, r2 ** 0.5)
    for (i, j) in ((i, j) for i in range(N) for j in range(i + 1, N)):
        p, q = (XY[i][0] + XY[j][0]) / 2, (XY[i][1] + XY[j][1]) / 2
        r2 = abs(XY[i][0] - p) ** 2 + abs(XY[i][1] - q) ** 2
        for l in range(N):
            x, y = XY[l]
            if r2 < abs(x - p) ** 2 + abs(y - q) ** 2 - EPS:
                break
        else:
            ans = min(ans, r2 ** 0.5)
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
