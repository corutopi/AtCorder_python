# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor

# inf = float('inf')
inf = 10 ** 18
mod = 10 ** 9 + 7
mod2 = 998244353


def warshall_floyd(N, ABC):
    """
    ワーシャルフロイド法の実行結果を返す.
    ノードは0始まりとする.
    計算量 O(max(N**3, len(ABT)).
    :param N: node num
    :param ABC: double list [[nodeA, nodeB, cost], ...]
    :return:
    """
    # inf = float('inf')
    re = [[0 if p == q else inf for p in range(N)] for q in range(N)]

    for a, b, c in ABC:
        re[a - 1][b - 1] = min(re[a - 1][b - 1], c)
        re[b - 1][a - 1] = min(re[b - 1][a - 1], c)

    for i in range(N):
        for j in range(N):
            for k in range(N):
                re[j][k] = min(re[j][k], re[j][i] + re[i][k])
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, ABC, K, XYZ):
    wf_map = warshall_floyd(N, ABC)
    S = sum((sum(wf) for wf in wf_map)) // 2
    for x, y, z in XYZ:
        x -= 1
        y -= 1
        if wf_map[x][y] > z:
            S -= wf_map[x][y] - z
            wf_map[x][y] = z
            wf_map[y][x] = z
            for i, j in ((i, j) for i in range(N) for j in range(i + 1, N)):
                tmp = min(wf_map[i][j],
                          wf_map[i][x] + wf_map[x][y] + wf_map[y][j],
                          wf_map[i][y] + wf_map[y][x] + wf_map[x][j])
                S -= wf_map[i][j] - tmp
                wf_map[i][j] = tmp
                wf_map[j][i] = tmp
        print(S)


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABC = [[int(i) for i in input().split()] for _ in range(M)]
    K = int(input())
    XYZ = [[int(i) for i in input().split()] for _ in range(K)]
    solve(N, M, ABC, K, XYZ)

    # # test
    # from random import randint
    # # import strings
    # # import tool.testcase as tt
    # # from tool.testcase import random_str, random_ints
    # N, M = 400, 1000
    # ABC = [[randint(1, N), randint(1, N), randint(1, 1000)] for _ in range(M)]
    # K = 400
    # XYZ = [[randint(1, N), randint(1, N), randint(1, 1000)] for _ in range(K)]
    # solve(N, M, ABC, K, XYZ)
