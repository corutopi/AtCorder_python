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
def solve(N, A):
    directed_graph = [[] for _ in range(N + 1)]
    edges = [0] * (N + 1)
    for i in range(N):
        directed_graph[i + 1].append(A[i])
        edges[i + 1] += 1
        edges[A[i]] += 1

    ans = []
    visited = [0] * (N + 1)
    start = 0

    def dfs(now):
        if visited[now] == 1:
            return now
        visited[now] = 1
        for dg in directed_graph[now]:
            tmp = dfs(dg)
            if tmp > 0:
                ans.append(now)
                if tmp == now:
                    return 0
                return tmp
        return 0

    for e in edges:
        if e > 1:
            dfs(e)
            if len(ans) > 0:
                print(len(ans))
                print(*ans[::-1])
                break


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
