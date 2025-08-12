# import sys
# sys.setrecursionlimit(10 ** 6)
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
def solve(N, M, A):
    naka = [[1] * N for _ in range(N)]

    for i in range(N):
        naka[i][i] = 0

    for a in A:
        for i in range(N - 1):
            x, y = a[i] - 1, a[i + 1] - 1
            naka[x][y] = 0
            naka[y][x] = 0

    print(sum(sum(n) for n in naka) // 2)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    A = [[int(i) for i in input().split()] for _ in range(M)]
    # P = [int(input()) for _ in range(N)]
    solve(N, M, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
