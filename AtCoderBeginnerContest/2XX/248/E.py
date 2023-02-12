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
        x = gcd(gcd(abs(a), abs(b)), abs(c))
        b //= x
        a //= x
        c //= x
        y = 1 if a > 0 else -1
        b *= y
        a *= y
        c *= y
    return a, b, c


def gcd(a, b):
    """最大公約数"""
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, XY):
    if K == 1:
        return 'Infinity'
    S = set()
    for i, j in ((i, j) for i in range(N) for j in range(N)):
        if i == j: continue
        abc = liner_function(*XY[i], *XY[j])
        S.add(' '.join((str(a) for a in abc)))
    ans = 0
    for s in S:
        a, b, c = map(int, s.split())
        cnt = 0
        for x, y in XY:
            cnt += 1 if a * x + b * y + c == 0 else 0
        ans += 1 if cnt >= K else 0
    return ans


def solve_explanation(N, K, XY):
    if K == 1:
        return 'Infinity'
    ans = 0
    flag = [[0] * N for _ in range(N)]
    for i, j in ((i, j) for i in range(N) for j in range(N)):
        if i == j: continue
        if flag[i][j]: continue
        cnt = 2
        flag[i][j] = 1
        flag[j][i] = 1
        x0, y0 = XY[i]
        x1, y1 = XY[j]
        for k in range(N):
            if i == k or j == k: continue
            x, y = XY[k]
            if (x1 - x0) * (y - y0) == (x - x0) * (y1 - y0):
                if flag[i][k] == 1:
                    cnt = 0
                    break
                cnt += 1
                flag[i][k] = 1
                flag[k][i] = 1
                flag[j][k] = 1
                flag[k][j] = 1
        ans += 1 if cnt >= K else 0
    return ans


if __name__ == '__main__':
    N, K = map(int, input().split())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    print(solve(N, K, XY))
    # print(solve_explanation(N, K, XY))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, K = 2, 2
    # XY = [[-2, -2], [0, -1]]
    # print(solve(N, K, XY))
    #
    # # N, K = 300, 3
    # # XY = [random_ints(2, -10 ** 9, 10 ** 9) for _ in range(N)]
    # while True:
    #     N = randint(1, 5)
    #     K = randint(1, N)
    #     XY = []
    #     while len(XY) < N:
    #         x, y = random_ints(2, -3, 3)
    #         for xx, yy in XY:
    #             if x == xx and y == yy: break
    #         else:
    #             XY.append([x, y])
    #     if solve_explanation(N, K, XY) != solve(N, K, XY):
    #         break
    # print(N, K)
    # print(XY)
    # print(solve(N, K, XY))
    # print(solve_explanation(N, K, XY))
