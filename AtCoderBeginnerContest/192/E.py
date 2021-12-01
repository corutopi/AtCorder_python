# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
from heapq import heappop, heappush

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, X, Y, ABTK):
    tree = [[] for _ in range(N + 1)]
    for a, b, t, k in ABTK:
        tree[a].append([b, t, k])
        tree[b].append([a, t, k])
    min_time = [inf] * (N + 1)
    hq = [[0, X]]
    while hq:
        time, now = heappop(hq)
        if min_time[now] <= time: continue
        min_time[now] = time
        for n, t, k in tree[now]:
            arrival = k * ceil(time / k) + t
            if min_time[n] > arrival:
                heappush(hq, [arrival, n])
    print(-1 if min_time[Y] == inf else min_time[Y])


if __name__ == '__main__':
    N, M, X, Y = map(int, input().split())
    ABTK = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, X, Y, ABTK)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, M = 10 ** 5, 10 ** 5
    # X, Y = randint(1, N), randint(1, N)
    # ABTK = []
    # for _ in range(M):
    #     a, b = 0, 0
    #     while a == b:
    #         a, b = randint(1, N), randint(1, N)
    #     ABTK.append([a, b, randint(1, 10 ** 9), randint(1, 10 ** 9)])
    # solve(N, M, X, Y, ABTK)
