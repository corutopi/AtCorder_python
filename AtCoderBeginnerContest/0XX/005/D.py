# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7


def divisor(x):
    """約数"""
    from math import floor
    re = []
    _x = floor(x ** 0.5)
    for i in range(1, _x + 1):
        if x % i == 0:
            re.append(i)
            if x // i != i:
                re.append(x // i)
    re.sort()
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, D, Q, P):
    D = [[0] * (N + 1)] + [[0] + d for d in D]
    dcs = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dcs[i][j] = D[i][j] + dcs[i - 1][j] + dcs[i][j - 1] - \
                        dcs[i - 1][j - 1]
    anses = [0] * (N ** 2 + 1)
    for i in range(1, N ** 2 + 1):
        tmp = 0
        divs = divisor(i)
        for p1 in divs:
            p2 = i // p1
            if p1 > N or p2 > N:
                continue
            for pp1 in range(p1, N + 1):
                for pp2 in range(p2, N + 1):
                    tmp = max(tmp,
                              dcs[pp1][pp2] -
                              dcs[pp1 - p1][pp2] - dcs[pp1][pp2 - p2] +
                              dcs[pp1 - p1][pp2 - p2])
        anses[i] = max(tmp, anses[i - 1])
    [print(anses[p]) for p in P]


if __name__ == '__main__':
    N = int(input())
    D = [[int(i) for i in input().split()] for _ in range(N)]
    Q = int(input())
    P = [int(input()) for _ in range(Q)]
    solve(N, D, Q, P)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 50
    # D = [[randint(1, 100) for _ in range(N)] for _ in range(N)]
    # Q = N ** 2
    # P = [randint(1, N ** 2) for _ in range(Q)]
    # solve(N, D, Q, P)
