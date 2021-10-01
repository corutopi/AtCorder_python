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
def solve(N, Q, AB, CD):
    tree = [[] for _ in range(N + 1)]
    for a, b in AB:
        tree[a].append(b)
        tree[b].append(a)
    from1 = [inf] * (N + 1)
    visited = [0] * (N + 1)

    def dfs(now, depth=0):
        visited[now] = 1
        from1[now] = depth
        for t in tree[now]:
            if visited[t] == 1: continue
            dfs(t, depth + 1)

    dfs(1)

    for c, d in CD:
        print('Town' if (from1[c] + from1[d]) % 2 == 0 else 'Road')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, Q = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    AB = [[int(i) for i in input().split()] for _ in range(N - 1)]
    CD = [[int(i) for i in input().split()] for _ in range(Q)]
    # P = [int(input()) for _ in range(N)]
    solve(N, Q, AB, CD)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
