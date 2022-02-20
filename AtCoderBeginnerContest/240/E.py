import sys

sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from math import ceil, floor

# inf = float('inf')
# mod = 10 ** 9 + 7
# mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, UV):
    tree_map = [[] for _ in range(N + 1)]
    for u, v in UV:
        # for _ in range(N - 1):
        #     u, v = map(int, input().split())
        tree_map[u].append(v)
        tree_map[v].append(u)

    ans = [() for _ in range(N + 1)]

    def dfs(n, p, s):
        if n != 1 and len(tree_map[n]) == 1:
            ans[n] = (s, s)
            return s
        e = s
        for x in tree_map[n]:
            if x == p: continue
            e = dfs(x, n, e)
            e += 1
        else:
            e -= 1
        ans[n] = (s, e)
        return e

    dfs(1, 0, 1)

    for a in ans[1:]:
        print(*a)


if __name__ == '__main__':
    N = int(input())
    UV = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, UV)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()

    # N = 2 * 10 ** 5
    # UV = [(i, i + 1) for i in range(1, N)]
    # solve(N, UV)
    # N = 2 * 10 ** 5
    # UV = [(1, i + 1) for i in range(1, N)]
    # solve(N, UV)
    # N = 2 * 10 ** 5
    # UV = [(i // 2, i) for i in range(2, N + 1)]
    # solve(N, UV)
