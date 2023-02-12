# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A):
    center = K ** 2 // 2 + 1

    def solver(x):
        cs_A = [[0] * (N + 1) for _ in range(N + 1)]
        for i, j in ((i, j) for i in range(1, N + 1) for j in range(1, N + 1)):
            cs_A[i][j] = cs_A[i - 1][j] + cs_A[i][j - 1] - cs_A[i - 1][j - 1] \
                         + (1 if A[i - 1][j - 1] > x else 0)
        for i, j in ((i, j) for i in range(K, N + 1) for j in range(K, N + 1)):
            if cs_A[i][j] - cs_A[i - K][j] - cs_A[i][j - K] + \
                    cs_A[i - K][j - K] < center:
                return True
        return False

    ok = max([max(a) for a in A])

    print(binary_search(ok, -1, solver))


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N, K = 800, 400
    # A = [[randint(1, 10 ** 9) for _ in range(N)] for _ in range(N)]
    # solve(N, K, A)
