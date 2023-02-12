"""
解説AC
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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, UV, S, T):
    graph = [[] for _ in range(N * 3)]
    for u, v in UV:
        u -= 1
        v -= 1
        graph[u * 3].append(v * 3 + 1)
        graph[u * 3 + 1].append(v * 3 + 2)
        graph[u * 3 + 2].append(v * 3)
    visited = [-1] * (N * 3)
    dq = deque([[(S - 1) * 3, 0]])
    while dq:
        now, cost = dq.popleft()
        for g in graph[now]:
            if visited[g] >= 0: continue
            dq.append([g, cost + 1])
            visited[g] = cost + 1
    print(visited[(T - 1) * 3] // 3 if visited[(T - 1) * 3] >= 0 else -1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [[int(i) for i in input().split()] for _ in range(M)]
    S, T = map(int, input().split())
    solve(N, M, UV, S, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # while True:
    #     N = 5
    #     M = randint(1, N * (N - 1))
    #     UV = [random_ints(2, 1, N) for _ in range(M)]
    #     S, T = random_ints(2, 1, N)
    #     solve(N, M, UV, S, T)
