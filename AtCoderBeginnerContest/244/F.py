"""
解説と提出 #30388578をもとに作成
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
from collections import deque
# import string
from math import ceil, floor

# inf = float('inf')
inf = 10 ** 9 + 7
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, UV):
    graph_map = [[] for _ in range(N + 1)]
    for u, v in UV:
        graph_map[u - 1].append(v - 1)
        graph_map[v - 1].append(u - 1)
    cost = [[inf] * N for _ in range(2 ** N)]
    cost[0] = [0] * N
    q = deque()
    for i in range(N):
        tmp = 1 << i
        cost[tmp][i] = 1
        q.append([tmp, i])

    while q:
        s, t = q.popleft()
        for g in graph_map[t]:
            next_s = s ^ 1 << g
            if cost[next_s][g] < inf:
                continue
            cost[next_s][g] = cost[s][t] + 1
            q.append([next_s, g])

    print(sum([min(c) for c in cost]))


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, UV)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
