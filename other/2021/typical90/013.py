# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
import heapq
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, ABC):
    from1tok = [inf] * (N + 1)
    fromNtok = [inf] * (N + 1)
    roadmap = [[] for _ in range(N + 1)]
    for a, b, c in ABC:
        roadmap[a].append([b, c])
        roadmap[b].append([a, c])

    hq = [[0, 1]]
    from1tok[1] = 0
    while hq:
        time, now = heapq.heappop(hq)
        for rm in roadmap[now]:
            if from1tok[rm[0]] > time + rm[1]:
                from1tok[rm[0]] = time + rm[1]
                heapq.heappush(hq, [time + rm[1], rm[0]])
    hq = [[0, N]]
    fromNtok[N] = 0
    while hq:
        time, now = heapq.heappop(hq)
        for rm in roadmap[now]:
            if fromNtok[rm[0]] > time + rm[1]:
                fromNtok[rm[0]] = time + rm[1]
                heapq.heappush(hq, [time + rm[1], rm[0]])

    for i in range(1, N + 1):
        print(from1tok[i] + fromNtok[i])


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABC = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, ABC)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
