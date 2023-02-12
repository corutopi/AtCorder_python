"""
解説を参考に作成
ワーシャルフロイド法
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, uvl):
    fw_map = [[inf] * (N + 1) for _ in range(N + 1)]
    top_near1 = []
    for u, v, l in uvl:
        if 1 in [u, v]:
            top_near1.append([max(u, v), l])
        else:
            fw_map[u][v] = l
            fw_map[v][u] = l

    for k in range(2, N + 1):
        for i in range(2, N + 1):
            for j in range(2, N + 1):
                fw_map[i][j] = min(fw_map[i][j], fw_map[i][k] + fw_map[j][k])

    ans = inf
    for i in range(len(top_near1)):
        for j in range(i + 1, len(top_near1)):
            top1, len1 = top_near1[i]
            top2, len2 = top_near1[j]
            ans = min(ans, fw_map[top1][top2] + len1 + len2)

    print(ans if ans < inf else -1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    uvl = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, uvl)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # N = 20
    # M = N * (N - 1) // 2
    # uvl = []
    # for _ in range(M):
    #     u = v = 0
    #     while u == v:
    #         u = randint(1, N)
    #         v = randint(1, N)
    #     l = randint(1, 1000)
    #     uvl.append([u, v, l])
    # solve(N, M, uvl)
