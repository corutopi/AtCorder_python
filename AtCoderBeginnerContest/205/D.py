# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = 10 ** 19
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
def solve(N, Q, A, K):
    A = [0] + A
    diffA = []
    for i in range(1, N + 1):
        diffA.append(A[i] - A[i - 1] - 1)
    cumsum_diffA = [0]
    for i in range(N):
        cumsum_diffA.append(cumsum_diffA[-1] + diffA[i])
    cumsum_diffA = cumsum_diffA + [inf]

    for k in K:
        tmp = binary_search(len(cumsum_diffA) - 1, -1, lambda x: cumsum_diffA[x] >= k)
        if tmp == len(cumsum_diffA) - 1:
            print(k + N)
        else:
            print(A[tmp] - (cumsum_diffA[tmp] - k + 1))


if __name__ == '__main__':
    N, Q = map(int, input().split())
    A = [int(i) for i in input().split()]
    K = [int(input()) for _ in range(Q)]
    solve(N, Q, A, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
