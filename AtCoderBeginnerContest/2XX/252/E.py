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
def solve(N, M, ABC):
    graph = [[] for _ in range(N + 1)]
    for i in range(M):
        a, b, c = ABC[i]
        graph[a].append([b, c, i + 1])
        graph[b].append([a, c, i + 1])

    road = [0] * (N + 1)
    cost = [0, 0] + [inf] * (N - 1)
    visited = [0] * (N + 1)
    hq = [[0, 1]]   # total cost, vertex
    while hq:
        tc, now = heappop(hq)
        if cost[now] < tc: continue
        if visited[now] == 1: continue
        visited[now] = 1
        for n, s, r in graph[now]:
            if cost[n] < tc + s: continue
            road[n] = r
            cost[n] = tc + s
            heappush(hq, [tc + s, n])
    print(*road[2:])


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
