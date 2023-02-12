"""
解説と以下を参考に作成
    https://atcoder.jp/contests/abc190/submissions/19826634
TLEに対する反省:
    内包表記をできるだけ使う
    検索時は in ではなく dict を使う
    無駄な for , if がないかちゃんと探す
"""
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
def solve(N, M, AB, K, C):
    tree = [[] for _ in range(N + 1)]
    for a, b in AB:
        tree[a].append(b)
        tree[b].append(a)

    dst_min = [[inf for _ in range(K)] for _ in range(K)]
    C_pnt = {C[i]: i for i in range(K)}
    for k in range(K):
        start = C[k]
        visited = [0] * (N + 1)
        dq = deque([(start, 0)])

        while dq:
            now, dst = dq.popleft()

            if visited[now]: continue

            visited[now] = 1
            if C_pnt.get(now, - 1) != -1:
                dst_min[k][C_pnt[now]] = dst

            for nxt in tree[now]:
                dq.append((nxt, dst + 1))

    if sum(dst_min[0]) == inf:
        print(-1)
        return

    dp = [[inf] * K for _ in range(2 ** K)]
    for i in range(1, 2 ** K):
        Cs = [j for j in range(K) if i >> j & 1]
        if len(Cs) == 1:
            dp[i][Cs[0]] = 0
            continue
        for s in Cs:
            tmp = i ^ (2 ** s)
            dp[i][s] = min([dp[tmp][x] + dst_min[x][s] for x in range(K)])

    print(min(dp[-1]) + 1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(M)]
    K = int(input())
    C = [int(i) for i in input().split()]
    solve(N, M, AB, K, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, M = 10 ** 5, 10 ** 5
    # AB = []
    # for i in range(1, N):
    #     AB.append([i, i + 1])
    # while len(AB) < M:
    #     a, b = randint(1, 10 ** 5), randint(1, 10 ** 5)
    #     if a == b:
    #         continue
    #     if a > b:
    #         a, b = b, a
    #     AB.append([a, b])
    # K = 17
    # C = []
    # while len(C) < K:
    #     tmp = randint(1, N)
    #     if tmp not in C:
    #         C.append(tmp)
    # solve(N, M, AB, K, C)
