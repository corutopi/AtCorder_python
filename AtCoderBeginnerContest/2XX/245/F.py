import sys
sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, UV):
    graph_map = [[] for _ in range(N)]
    for u, v in UV:
        graph_map[u - 1].append(v - 1)
    visited = [0] * N
    isloop = [0] * N

    def dfs(now):
        visited[now] = 1
        loop_status = -1
        for g in graph_map[now]:
            if visited[g] == 1:
                if isloop[g] >= 0:
                    loop_status = 1
                elif loop_status == 0:
                    loop_status = -1
            else:
                tmp = dfs(g)
                if tmp == 1 or (tmp == -1 and loop_status == 0):
                    loop_status = tmp
        isloop[now] = loop_status
        return loop_status

    for i in range(N):
        if visited[i] == 1: continue
        dfs(i)

    print(sum([1 if i == 1 else 0 for i in isloop]))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    UV = [[int(i) for i in input().split()] for _ in range(M)]
    # P = [int(input()) for _ in range(N)]
    solve(N, M, UV)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
