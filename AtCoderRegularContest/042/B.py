# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque


def liner_function(x1, y1, x2, y2):
    """return a, b, c of ax + by + c = 0.
    b = 0 or 1
    x1 != x2 or y1 != y2
    :param x1: meet y1 = ax1 + b
    :param y1:
    :param x2: meet y2 = ax2 + b
    :param y2:
    :return:
    """
    if x1 == x2:
        a = 1
        b = 0
        c = - x1
    elif y1 == y2:
        a = 0
        b = 1
        c = - y1
    else:
        b = 1
        a = - (y1 - y2) / (x1 - x2)
        c = - a * x1 - b * y1
    return a, b, c


def vertical_line(a, b, c, x, y):
    """retrun a1, b1, c1 of 'a1x + b1y + c = 0' intersect 'ax + by + c = 0' vertically.

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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(X, Y, N, XY):
    ans = 10 ** 18
    for i in range(N):
        ii = i + 1
        if i == N - 1:
            ii = 0
        a, b, c = liner_function(XY[i][0], XY[i][1], XY[ii][0], XY[ii][1])
        aa, bb, cc = vertical_line(a, b, c, X, Y)
        x, y = liner_cross_point(a, b, c, aa, bb, cc)
        if not (min(XY[i][0], XY[ii][0]) <= x <= max(XY[i][0], XY[ii][0])):
            x, y = XY[i] if abs(x - XY[i][0]) <= abs(x - XY[ii][0]) else XY[ii]
        kyori = (abs(X - x) ** 2 + abs(Y - y) ** 2) ** 0.5
        ans = min(ans, (abs(X - x) ** 2 + abs(Y - y) ** 2) ** 0.5)
    print(ans)


if __name__ == '__main__':
    X, Y = map(int, input().split())
    N = int(input())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(X, Y, N, XY)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
