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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(B, C):
    mass = [[-1] * 3 for _ in range(3)]

    def dfs(x):
        mr, ms = 0, 0
        if x == 9:
            return point()
        m = x % 2
        for i, j in ((i, j) for i in range(3) for j in range(3)):
            if mass[i][j] != -1: continue
            mass[i][j] = m
            tmr, tms = dfs(x + 1)
            mass[i][j] = -1
            if m == 0:
                mr, ms = (tmr, tms) if tmr >= mr else (mr, ms)
            else:
                mr, ms = (tmr, tms) if tms >= ms else (mr, ms)
        return mr, ms

    def point():
        mr, ms = 0, 0
        for i, j in ((i, j) for i in range(2) for j in range(3)):
            if mass[i][j] == mass[i+1][j]:
                mr += B[i][j]
            else:
                ms += B[i][j]
        for i, j in ((i, j) for i in range(3) for j in range(2)):
            if mass[i][j] == mass[i][j+1]:
                mr += C[i][j]
            else:
                ms += C[i][j]
        return mr, ms

    [print(d) for d in dfs(0)]


if __name__ == '__main__':
    B = [[int(i) for i in input().split()] for _ in range(2)]
    C = [[int(i) for i in input().split()] for _ in range(3)]
    solve(B, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
