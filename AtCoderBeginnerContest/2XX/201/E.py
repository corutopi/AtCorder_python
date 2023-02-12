"""
解説sub
"""
import sys

sys.setrecursionlimit(10 ** 6)
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
def solve(N, UVW):
    tree_map = [[] for _ in range(N)]
    for u, v, w in UVW:
        u -= 1
        v -= 1
        tree_map[u].append([v, w])
        tree_map[v].append([u, w])

    dist0 = [0] * N
    dq = deque([[0, -1]])
    while dq:
        now, parent = dq.popleft()
        for nxt, w in tree_map[now]:
            if nxt == parent: continue
            dist0[nxt] = dist0[now] ^ w
            dq.append([nxt, now])

    ans = 0
    for i in range(60):
        ans += sum(1 for d in dist0 if (d >> i & 1)) * \
               sum(1 for d in dist0 if not (d >> i & 1)) * \
               pow(2, i, mod)
        ans %= mod
    print(ans)


if __name__ == '__main__':
    N = int(input())
    UVW = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, UVW)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
