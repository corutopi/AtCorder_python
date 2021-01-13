# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, abt):
    wf = [[inf if p != q else 0 for p in range(N + 1)] for q in range(N + 1)]
    for a, b, t in abt:
        wf[a][b] = t
        wf[b][a] = t

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                wf[j][k] = min(wf[j][k], wf[j][i] + wf[i][k])

    print(min([max(wfx[1:]) for wfx in wf]))


if __name__ == '__main__':
    N, M = map(int, input().split())
    abt = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, abt)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
