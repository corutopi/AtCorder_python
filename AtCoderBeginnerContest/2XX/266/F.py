"""
解説Sub
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

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, uv, Q, xy):
    graph = [[] for _ in range(N)]
    edge_num = [0] * N
    is_cycle = [True] * N
    for u, v in uv:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
        edge_num[u] += 1
        edge_num[v] += 1
    for i in [i for i in range(N) if edge_num[i] == 1]:
        dq = deque([i])
        while dq:
            now = dq.popleft()
            is_cycle[now] = False
            for nxt in graph[now]:
                edge_num[nxt] -= 1
                if edge_num[nxt] == 1:
                    dq.append(nxt)
    leaf_number = [-1] * N
    for i in range(N):
        if not is_cycle[i]: continue
        leaf_number[i] = i
        dq = deque([[i, -1]])
        while dq:
            now, pnt = dq.popleft()
            leaf_number[now] = i
            for nxt in graph[now]:
                if is_cycle[nxt]: continue
                if nxt == pnt: continue
                dq.append([nxt, now])

    for x, y in xy:
        x -= 1
        y -= 1
        print('Yes' if leaf_number[x] == leaf_number[y] else 'No')


if __name__ == '__main__':
    N = int(input())
    uv = [[int(i) for i in input().split()] for _ in range(N)]
    Q = int(input())
    xy = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, uv, Q, xy)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
