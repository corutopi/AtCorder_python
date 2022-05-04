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
def solve(N, AB):
    tree = [[] for _ in range(N + 1)]
    for a, b in AB:
        tree[a].append(b)
        tree[b].append(a)
    parent = [-1] * (N + 1)
    parent[1] = 0
    ans = [[-1, -1] for _ in range(N + 1)]

    def dfs(n):
        # calc n pattern two color
        w = 1
        b = 1
        for t in tree[n]:
            if t == parent[n]: continue
            parent[t] = n
            if ans[t][0] == -1 or ans[t][1] == -1:
                dfs(t)
            w *= sum(ans[t])
            w %= mod
            b *= ans[t][0]   # only white child
            b %= mod
        ans[n] = [w, b]

    dfs(1)

    print(sum(ans[1]) % mod)


if __name__ == '__main__':
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
