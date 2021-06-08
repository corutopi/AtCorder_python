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
def solve(N, A, Q, B):
    A.sort()
    A += [10 ** 18]

    def isbig(x):
        return b >= A[x]

    def issmall(x):
        return b <= A[x]

    for b in B:
        x = binary_search(0, N, isbig)
        y = binary_search(N, 0, issmall)
        print(min(abs(b - A[x]), abs(b - A[y])))


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    B = [int(input()) for _ in range(Q)]
    solve(N, A, Q, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 3 * 10 ** 5
    # A = random_ints(N, 0, 10 ** 9)
    # Q = 3 * 10 ** 5
    # B = random_ints(Q, 0, 10 ** 9)
    # solve(N, A, Q, B)
