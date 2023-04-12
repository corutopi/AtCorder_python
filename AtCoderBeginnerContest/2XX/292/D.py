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
def solve(N, M, uv):
    graph = [[] for _ in range(N)]
    for u, v in uv:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    visited = [0] * N
    for i in range(N):
        if visited[i]: continue
        vertex = 0
        edge = 0
        q = deque([i])
        while q:
            now = q.popleft()
            if visited[now]: continue
            visited[now] = 1
            vertex += 1
            edge += len(graph[now])
            for g in graph[now]:
                if visited[g]: continue
                q.append(g)
        if vertex * 2 != edge:
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    N, M = map(int, input().split())
    uv = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, uv)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
