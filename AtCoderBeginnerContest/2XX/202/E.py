# 解説を参考に作成
import sys

sys.setrecursionlimit(10 ** 6)
import bisect
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
def solve(N, P, Q, UD):
    tree = [[] for _ in range(N + 1)]  # only child
    for i, p in enumerate(P, 2):
        tree[p].append(i)

    inout = [[0, 0] for _ in range(N + 1)]
    inlist = [[] for _ in range(N + 1)]

    def dfs(now, depth, cnt):
        inout[now][0] = cnt
        inlist[depth].append(cnt)
        for t in tree[now]:
            cnt = dfs(t, depth + 1, cnt + 1)
        cnt += 1
        inout[now][1] = cnt
        return cnt

    dfs(1, 0, 0)

    for u, d in UD:
        print(bisect.bisect_right(inlist[d], inout[u][1]) -
              bisect.bisect_left(inlist[d], inout[u][0]))


if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]
    Q = int(input())
    UD = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, P, Q, UD)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
