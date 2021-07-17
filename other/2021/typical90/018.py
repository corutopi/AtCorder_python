# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def circle_point(t, T, L):
    """t分後の座標x, y, zを返す"""
    from math import sin, cos, radians
    r = L / 2
    angle = 270 - (t * (360 / T))
    angle = angle if angle >= 0 else 360 + angle
    x, y, z = 0, cos(radians(angle)) * r, sin(radians(angle)) * r + r
    return x, y, z


def depression_angle_3d(x1, y1, z1, x2, y2, z2):
    """z軸を垂直方向とする3次元立面で座標1から見た時の座標2の俯角を返す.
    "俯角"を表すため, 座標2が座標1より上側にある場合, 角度は負になる.
    """
    from math import sqrt, degrees, atan
    c = sqrt((x1 - x2) ** 2 +
             (y1 - y2) ** 2 +
             (z1 - z2) ** 2)
    a = sqrt((z1 - z2) ** 2)
    b = sqrt((c ** 2) - (a ** 2))
    return degrees(atan(a / b)) * (1 if z1 >= z2 else -1)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(T, L, X, Y, Q, E):
    for e in E:
        x, y, z = circle_point(e, T, L)
        print(depression_angle_3d(x, y, z, X, Y, 0))


if __name__ == '__main__':
    T = int(input())
    L, X, Y = map(int, input().split())
    Q = int(input())
    E = [int(input()) for _ in range(Q)]
    solve(T, L, X, Y, Q, E)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
