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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, N):
    grid = [['.'] * W for _ in range(H)]
    i, j = 0, 0
    vector = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    v = 0
    for _ in range(N):
        if grid[i][j] == '.':
            grid[i][j] = '#'
            v = (v + 1) % 4
            i = (i + vector[v][0]) % H
            j = (j + vector[v][1]) % W
        else:
            grid[i][j] = '.'
            v = (v - 1) % 4
            i = (i + vector[v][0]) % H
            j = (j + vector[v][1]) % W
    for g in grid:
        print(''.join(g))


if __name__ == '__main__':
    H, W, N = map(int, input().split())
    solve(H, W, N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
