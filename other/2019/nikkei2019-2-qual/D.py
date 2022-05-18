# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from heapq import heappush, heappop
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, LRC):
    pointer = [[] for _ in range(N)]
    for l, r, c in LRC:
        pointer[l - 1].append([c, r - 1])
    cost = [-1] * N
    hq = [[0, 0]]
    for i in range(N):
        if not hq: break
        cost[i] = hq[0][0]
        while hq and hq[0][1] <= i:
            heappop(hq)
        for p in pointer[i]:
            heappush(hq, [cost[i] + p[0], p[1]])
    print(cost[-1])


if __name__ == '__main__':
    N, M = map(int, input().split())
    LRC = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, LRC)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
