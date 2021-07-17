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
def solve(N, AB):
    treemap = [[] for _ in range(N + 1)]
    for a, b in AB:
        treemap[a].append(b)
        treemap[b].append(a)

    visited = [0] * (N + 1)
    set1 = []
    set2 = []
    dq = deque([[1, 0, True]])
    while dq:
        now, s, parent = dq.popleft()
        if s:
            set1.append(now)
        else:
            set2.append(now)

        for t in treemap[now]:
            if t == parent: continue
            dq.append([t, not s, now])
    useset = set1 if len(set1) >= N // 2 else set2
    print(' '.join([str(u) for u in useset][:(N // 2)]))


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
