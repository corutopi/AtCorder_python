# 解説AC
# ダイクストラのポテンシャル
# https://qiita.com/ngtkana/items/d7fc4463e56b966d1ebf

import sys

sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def bellman_ford(N, ABT, start=0, isdirected=True):
    from collections import deque

    inf = float('inf')
    graph_map = [[] for _ in range(N)]
    re = [inf] * N
    for a, b, t in ABT:
        graph_map[a].append([b, t])
        if not isdirected:
            graph_map[b].append([a, t])
    re[start] = 0
    for _ in range(N - 1):
        dq = deque([start])
        while dq:
            now = dq.popleft()
            for n, t in graph_map[now]:
                if re[now] + t < re[n]:
                    re[n] = re[now] + t
                    dq.append(n)
    return re


def dijkstra(N, ABC, start=0):
    from heapq import heappush, heappop

    inf = float('inf')
    graph_map = [[] for _ in range(N)]
    re = [inf] * N
    for a, b, c in ABC:
        graph_map[a].append([b, c])
    re[start] = 0
    visited = [0] * N
    hq = [[0, start]]
    while hq:
        cost, now = heappop(hq)
        if visited[now]: continue
        visited[now] = 1
        for nxt, c in graph_map[now]:
            if re[now] + c < re[nxt]:
                re[nxt] = re[now] + c
                heappush(hq, [re[nxt], nxt])
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, H, UV):
    graph_map = [[] for _ in range(N)]
    for u, v in UV:
        graph_map[u - 1].append(v - 1)
        graph_map[v - 1].append(u - 1)
    ABC = []
    for u, v in UV:
        u, v = u - 1, v - 1
        if H[u] < H[v]:
            u, v = v, u
        ABC.append([u, v, -(H[u] - H[v]) - (H[v] - H[u])])
        ABC.append([v, u, 2 * (H[u] - H[v]) - (H[u] - H[v])])
    d = dijkstra(N, ABC)
    d = [d[i] + (H[i] - H[0]) for i in range(len(d))]
    print(-min(d))
    # return -min(d)


def force_solve(N, M, H, UV):
    ABT = []
    for u, v in UV:
        u, v = u - 1, v - 1
        if H[u] <= H[v]:
            u, v = v, u
        ABT.append([u, v, - (H[u] - H[v])])
        ABT.append([v, u, 2 * (H[u] - H[v])])
    bf = bellman_ford(N, ABT)
    # print(-min(bf))
    return -min(bf)


if __name__ == '__main__':
    N, M = map(int, input().split())
    H = [int(i) for i in input().split()]
    UV = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, H, UV)
    # force_solve(N, M, H, UV)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints

    # N, M = 6, 10
    # H = [4, 9, 4, 3, 5, 2]
    # UV = [[2, 5], [3, 5], [2, 6], [1, 3], [4, 5], [2, 3], [1, 2], [2, 4],
    #       [4, 6], [5, 6]]
    # print(solve(N, M, H, UV))
    # print(force_solve(N, M, H, UV))

    # while True:
    #     N, M = 6, 10
    #     H = random_ints(N, 1, 10)
    #     UV = tt.make_test_graph_data(N, M)
    #     if solve(N, M, H, UV) != force_solve(N, M, H, UV):
    #         print(N, M)
    #         print(H)
    #         print(UV)
    #         break
