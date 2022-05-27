# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
from collections import deque
# import string
from math import ceil, floor
from heapq import heappush, heappop

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, S, T, UVAB):
    S -= 1
    T -= 1
    graph = [[] for _ in range(N)]
    for u, v, a, b in UVAB:
        graph[u - 1].append([v - 1, a, b])
        graph[v - 1].append([u - 1, a, b])
    # s -> 各都市に円でダイクストラ
    yhq = [[0, S]]
    yen = [inf] * N
    while yhq:
        yc, yn = heappop(yhq)
        if yc > yen[yn]: continue
        yen[yn] = yc
        for ynext, ya, yb in graph[yn]:
            if yc + ya < yen[ynext]:
                yen[ynext] = yc + ya
                heappush(yhq, [yc + ya, ynext])
    # t -> 各都市にスヌークでダイクストラ
    shq = [[0, T]]
    snk = [inf] * N
    while shq:
        sc, sn = heappop(shq)
        if sc > snk[sn]: continue
        snk[sn] = sc
        for snext, sa, sb in graph[sn]:
            if sc + sb < snk[snext]:
                snk[snext] = sc + sb
                heappush(shq, [sc + sb, snext])
    # 合計値が最終かかる金額と考えてよい
    cost = [[yen[i] + snk[i], i] for i in range(N)]
    cost.sort()
    cost = deque(cost)
    # 0 ~ N-1 についてスライド最小値で求める
    for j in range(N):
        while cost[0][1] < j:
            cost.popleft()
        print(10 ** 15 - cost[0][0])


if __name__ == '__main__':
    N, M, S, T = map(int, input().split())
    UVAB = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, S, T, UVAB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
