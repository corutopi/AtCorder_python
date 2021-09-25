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
    tree = [[] for _ in range(N + 1)]
    for a, b in AB:
        tree[a].append(b)
        tree[b].append(a)
    [t.sort() for t in tree]

    visited = [0] * (N + 1)
    ans = []

    def dfs(now):
        ans.append(str(now))
        visited[now] = 1
        for i in tree[now]:
            if visited[i] == 1: continue
            dfs(i)
            ans.append(str(now))

    dfs(1)
    print(' '.join(ans))


if __name__ == '__main__':
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N - 1)]
    solve(N, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import *
    #
    # N = 10
    # while True:
    #     solve(N, make_tree_data(N))
