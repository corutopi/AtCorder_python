# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, UV):
    tree = [[] for _ in range(N + 1)]
    for u, v in UV:
        tree[u].append(v)
        tree[v].append(u)
    visited = [0] * (N + 1)
    roop = 0
    for i in range(1, N + 1):
        if visited[i]: continue
        dq = deque([[i, 0]])
        cnt = 0
        while dq:
            now, parent = dq.popleft()
            visited[now] = 1
            for t in tree[now]:
                if t == parent: continue
                if visited[t]:
                    cnt += 1
                    continue
                dq.append([t, now])
        if cnt != 2:
            print(0)
            return
        roop += 1
    print(pow(2, roop, mod2))


if __name__ == '__main__':
    N, M = map(int, input().split())
    UV = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, UV)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
