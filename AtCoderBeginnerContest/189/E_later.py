"""
解説を参考に作成
#アフィン変換
##行列で計算していると間に合わない
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
import numpy as np

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def unit_matrix():
    return np.array([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]], dtype='int64')


def invert_x(p=0):
    """
    x = p の直線で反転させるアフィン変換行列
    :param p:
    :return:
    """
    return np.array([[-1, 0, 2 * p],
                     [0, 1, 0],
                     [0, 0, 1]], dtype='int64')


def invert_y(p=0):
    """
    y = p の直線で反転させるアフィン変換行列
    :param p:
    :return:
    """
    return np.array([[1, 0, 0],
                     [0, -1, 2 * p],
                     [0, 0, 1]], dtype='int64')


def turn_right90():
    """
    90度右回転させるアフィン変換行列
    :return:
    """
    return np.array([[0, 1, 0],
                     [-1, 0, 0],
                     [0, 0, 1]], dtype='int64')


def turn_left90():
    """
    90度左回転させるアフィン変換行列
    :return:
    """
    return np.array([[0, -1, 0],
                     [1, 0, 0],
                     [0, 0, 1]], dtype='int64')


from decorator import stop_watch


@stop_watch
def solve(N, XY, M, op, Q, AB):
    XY1 = [np.array(xy + [1]) for xy in XY]
    matrix = [unit_matrix()]
    for opi in op:
        if opi[0] == 1:
            matrix.append(np.dot(turn_right90(), matrix[-1]))
        elif opi[0] == 2:
            matrix.append(np.dot(turn_left90(), matrix[-1]))
        elif opi[0] == 3:
            matrix.append(np.dot(invert_x(opi[1]), matrix[-1]))
        elif opi[0] == 4:
            matrix.append(np.dot(invert_y(opi[1]), matrix[-1]))

    for a, b in AB:
        ans = np.dot(matrix[a], XY1[b - 1])
        # print(ans[0], ans[1])


if __name__ == '__main__':
    # N = int(input())
    # XY = [[int(i) for i in input().split()] for _ in range(N)]
    # K = int(input())
    # op = [[int(i) for i in input().split()] for _ in range(K)]
    # Q = int(input())
    # AB = [[int(i) for i in input().split()] for _ in range(Q)]
    # solve(N, XY, K, op, Q, AB)

    # test
    from random import randint
    import string
    import tool.testcase as tt
    from tool.testcase import random_str, random_ints
    N = 2 * 10 ** 5
    XY = [[randint(- 10 ** 9, 10 ** 9) for _ in range(2)] for _ in range(N)]
    M = 2 * 10 ** 5
    op = []
    for _ in range(M):
        o = [randint(1, 4)]
        if o[0] >= 3: o.append(randint(- 10 ** 9, 10 ** 9))
        op.append(o)
    Q = 2 * 10 ** 5
    AB = [[randint(1, M), randint(1, N)] for _ in range(Q)]
    solve(N, XY, M, op, Q, AB)
