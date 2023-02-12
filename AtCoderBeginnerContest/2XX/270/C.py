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
def solve(N, X, Y, UV):
    tree = [[] for _ in range(N + 1)]
    for u, v in UV:
        tree[u].append(v)
        tree[v].append(u)

    def bfs(now, parent=0):
        if now == X:
            print(now)
            return True

        for nxt in tree[now]:
            if nxt == parent: continue
            if bfs(nxt, now):
                print(now)
                return True

        return False

    bfs(Y)


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    UV = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, X, Y, UV)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
