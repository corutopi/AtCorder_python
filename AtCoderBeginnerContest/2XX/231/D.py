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
def solve(N, M, AB):
    graph = [[] for _ in range(N)]
    visited = [0] * N
    for a, b in AB:
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        if visited[i]: continue
        dq = deque([[i, -1]])
        while dq:
            now, parent = dq.popleft()
            if visited[now]:
                print('No')
                return
            if len(graph[now]) >= 3:
                print('No')
                return
            visited[now] = 1
            for nxt in graph[now]:
                if nxt == parent: continue
                dq.append([nxt, now])
    print('Yes')


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve(7, 5, [[5, 7], [4, 5], [5, 7], [4, 5], [2, 7]])
    # while True:
    #     N = 7
    #     M = randint(1, 7)
    #     AB = []
    #     while len(AB) < M:
    #         A = randint(1, N - 1)
    #         B = randint(A + 1, N)
    #         AB.append([A, B])
    #     print(AB)
    #     solve(N, M, AB)
