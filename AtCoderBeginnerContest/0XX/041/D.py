"""
解説AC
"""
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
def solve(N, M, XY):
    directed_graph = [[] for _ in range(N)]
    for x, y in XY:
        directed_graph[x - 1].append(y - 1)
    dp = [0] * (2 ** N)
    dp[0] = 1
    for i in range(1, 2 ** N):
        FLG = []
        V = []
        for j in range(N):
            x = i >> j & 1
            FLG.append(x)
            if x == 1: V.append(j)
        for v in V:
            for dg in directed_graph[v]:
                if FLG[dg] == 1:
                    break
            else:
                dp[i] += dp[i ^ (2 ** v)]
    print(dp[-1])


if __name__ == '__main__':
    N, M = map(int, input().split())
    XY = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, XY)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
