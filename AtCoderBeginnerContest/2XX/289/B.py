# import sys
# sys.setrecursionlimit(10 ** 6)
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
def solve(N, M, a):
    tree = [[] for _ in range(N + 1)]
    for aa in a:
        tree[aa].append(aa + 1)
    visited = [0] * (N + 1)
    ans = []

    def dfs(now):
        visited[now] = 1
        for t in tree[now]:
            dfs(t)
        ans.append(now)

    for i in range(1, N + 1):
        if visited[i]: continue
        dfs(i)

    print(*ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    a = [int(i) for i in input().split()]
    solve(N, M, a)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
