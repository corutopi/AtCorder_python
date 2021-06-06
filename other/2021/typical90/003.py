import sys

sys.setrecursionlimit(10 ** 6)
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
    tree_map = [[] for _ in range(N + 1)]
    for a, b in AB:
        tree_map[a].append(b)
        tree_map[b].append(a)

    ans = [0]

    def dfs(x, parent):
        # global ans
        child_depth = []
        for t in tree_map[x]:
            if t == parent:
                continue
            child_depth.append(dfs(t, x))
        if len(child_depth) == 0: return 1
        child_depth.sort(reverse=True)
        ans[0] = max(ans[0], child_depth[0] if len(child_depth) == 0 \
            else sum(child_depth[:2]))
        return max(child_depth) + 1

    dfs(1, 0)
    print(ans[0] + 1)


if __name__ == '__main__':
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 10 ** 5
    # AB = [[i, i + 1] for i in range(1, 10 ** 5)]
    # solve(N, AB)
