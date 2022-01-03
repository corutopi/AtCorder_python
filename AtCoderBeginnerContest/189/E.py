"""
解説を参考に作成
#アフィン変換
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

# import numpy as np

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

unit = [[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]]
turn_right = [[0, 1, 0],
              [-1, 0, 0],
              [0, 0, 1]]
turn_left = [[0, -1, 0],
             [1, 0, 0],
             [0, 0, 1]]


def unit_matrix():
    return [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]


def invert_x(p=0):
    """
    x = p の直線で反転させるアフィン変換行列
    :param p:
    :return:
    """
    return [[-1, 0, 2 * p],
            [0, 1, 0],
            [0, 0, 1]]


def invert_y(p=0):
    """
    y = p の直線で反転させるアフィン変換行列
    :param p:
    :return:
    """
    return [[1, 0, 0],
            [0, -1, 2 * p],
            [0, 0, 1]]


def turn_right90():
    """
    90度右回転させるアフィン変換行列
    :return:
    """
    return [[0, 1, 0],
            [-1, 0, 0],
            [0, 0, 1]]


def turn_left90():
    """
    90度左回転させるアフィン変換行列
    :return:
    """
    return [[0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]]


def matrix_q(arr1, arr2):
    r = len(arr1)
    c = len(arr2[0])
    re = [[0] * c for _ in range(r)]
    for i, j in ((i, j) for i in range(r) for j in range(c)):
        re[i][j] = sum([arr1[i][k] * arr2[k][j] for k in range(r)])
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, XY, M, op, Q, AB):
    mtx = [[[0, 0], [1, 0], [0, 1]]]
    for o in op:
        e, f, g = mtx[-1]
        if o[0] == 1:
            e = [e[1], -e[0]]
            f = [f[1], -f[0]]
            g = [g[1], -g[0]]
        if o[0] == 2:
            e = [-e[1], e[0]]
            f = [-f[1], f[0]]
            g = [-g[1], g[0]]
        if o[0] == 3:
            e = [o[1] * 2 - e[0], e[1]]
            f = [o[1] * 2 - f[0], f[1]]
            g = [o[1] * 2 - g[0], g[1]]
        if o[0] == 4:
            e = [e[0], o[1] * 2 - e[1]]
            f = [f[0], o[1] * 2 - f[1]]
            g = [g[0], o[1] * 2 - g[1]]
        mtx.append([e, f, g])
    for a, b in AB:
        e, f, g = mtx[a]
        x, y = XY[b - 1]
        if e[0] == f[0]:
            nx = (g[0] - e[0]) * y + e[0]
            ny = (f[1] - e[1]) * x + e[1]
        else:
            nx = (f[0] - e[0]) * x + e[0]
            ny = (g[1] - e[1]) * y + e[1]
        print(nx, ny)


if __name__ == '__main__':
    N = int(input())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    M = int(input())
    op = [[int(i) for i in input().split()] for _ in range(M)]
    Q = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, XY, M, op, Q, AB)

    # # test
    # from random import randint
    # # import string
    # # import tool.testcase as tt
    # # from tool.testcase import random_str, random_ints
    #
    # N = 2 * 10 ** 5
    # XY = [[randint(- 10 ** 9, 10 ** 9) for _ in range(2)] for _ in range(N)]
    # M = 2 * 10 ** 5
    # op = []
    # for _ in range(M):
    #     o = [randint(1, 4)]
    #     if o[0] >= 3: o.append(randint(- 10 ** 9, 10 ** 9))
    #     op.append(o)
    # Q = 2 * 10 ** 5
    # AB = [[randint(1, M), randint(1, N)] for _ in range(Q)]
    # solve(N, XY, M, op, Q, AB)
