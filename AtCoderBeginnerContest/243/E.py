# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def warshall_floyd(N, ABC):
    """
    ワーシャルフロイド法の実行結果を返す.
    ノードは1始まりとする.
    計算量 O(max(N**3, len(ABT)).
    :param N: node num
    :param ABC: double list [[nodeA, nodeB, cost], ...]
    :return:
    """
    inf = float('inf')
    re = [[0 if p == q else inf for p in range(N)] for q in range(N)]
    org = [[1 for _ in range(N)] for _ in range(N)]

    for a, b, c in ABC:
        a -= 1
        b -= 1
        re[a][b] = min(re[a][b], c)
        re[b][a] = min(re[b][a], c)
        org[a][b] = 0
        org[b][a] = 0

    cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                if j == i or i == k: continue
                if re[j][k] >= re[j][i] + re[i][k] and org[j][k] == 0:
                    cnt += 1
                    org[j][k] = 1
                    org[k][j] = 1
                re[j][k] = min(re[j][k], re[j][i] + re[i][k])

    return cnt


# from decorator import stop_watch
#
#
# @stop_watch
def solve():
    print('ans')


if __name__ == '__main__':
    N, M = map(int, input().split())
    ABC = [[int(i) for i in input().split()] for _ in range(M)]
    print(warshall_floyd(N, ABC))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
