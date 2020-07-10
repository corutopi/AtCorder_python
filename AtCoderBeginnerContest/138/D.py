import sys
sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Q, ABs, PXs):
    tree_map = [[] for _ in range(N + 1)]
    for a, b in ABs:
        tree_map[a].append(b)
        tree_map[b].append(a)

    ans = [0 for _ in range(N + 1)]
    for p, x in PXs:
        ans[p] += x

    def dfs(v, r):  # vertex, root
        ans[v] += ans[r]
        for tm in tree_map[v]:
            if tm == r:
                continue
            dfs(tm, v)

    dfs(1, 0)

    for a in ans[1:]:
        print(a)


if __name__ == '__main__':
    N, Q = map(int, input().split())
    ABs = [[int(i) for i in input().split()] for _ in range(N - 1)]
    PXs = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, ABs, PXs)
