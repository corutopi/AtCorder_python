# 解説を見て作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque


def binary_search(ok, ng, solve):
    """2分探索"""
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
def solve(N, M, V, P, A):
    A = [- 10 ** 18] + A
    A.sort()
    key = A[N - P + 1]

    def solver(m):
        if A[m] >= key:
            return True
        if A[m] + M < key:
            return False
        point_sum = 0
        for i in range(1, N + 1):
            x = 0
            if i == m:
                continue
            elif i > N - P + 1:
                x = M
            else:
                x = min(M, max(0, A[m] + M - A[i]))
            point_sum += x
        return True if point_sum >= M * (V - 1) else False

    print(N - binary_search(N, 0, solver) + 1)


if __name__ == '__main__':
    N, M, V, P = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, M, V, P, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
