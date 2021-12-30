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
def solve(N, M, AB):
    revers_tree = [[] for _ in range(N + 1)]
    revers_directed = [0] * (N + 1)
    for a, b in AB:
        revers_tree[b].append(a)
        revers_directed[a] += 1
    parent = [-1] * (N + 1)
    depth = [-1] * (N + 1)

    def dfs(x):
        if depth[x] != -1:
            pass
        elif len(revers_tree[x]) == 0:
            parent[x] = 0
            depth[x] = 0
            pass
        else:
            for rt in revers_tree[x]:
                tmp_d = dfs(rt) + 1
                if depth[x] == -1 or tmp_d > depth[x]:
                    parent[x] = rt
                    depth[x] = tmp_d
        return depth[x]

    for i in range(1, N + 1):
        if revers_directed[i] != 0: continue
        dfs(i)

    [print(i) for i in parent[1:]]


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N - 1 + M)]
    solve(N, M, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints

    # N, M = 10 ** 5, 0
    # # AB = tt.make_tree_data(N, 1)
    # AB = [[i, i + 1] for i in range(1, N)]
    # solve(N, M, AB)
