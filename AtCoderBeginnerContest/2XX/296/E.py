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
def solve(N, A):
    """
    - i ∈ A でない場合, 青木の勝ち
    - i ∈ A の場合
        - ループに含まれる場合, 高橋の勝ち
        - 含まれない場合, 青木の勝ち
    """
    graph = [[] for _ in range(N + 1)]
    indeg = [0] * (N + 1)
    visited = [0] * (N + 1)
    for i in range(N):
        x, y = A[i], i + 1
        indeg[x] += 1
        graph[y].append(x)
    for i in range(N + 1):
        if indeg[i] > 0: continue
        if visited[i] == 1: continue
        q = deque([i])
        while q:
            x = q.popleft()
            visited[x] = 1
            for g in graph[x]:
                indeg[g] -= 1
                if indeg[g] == 0:
                    q.append(g)
    print(sum(indeg))


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
