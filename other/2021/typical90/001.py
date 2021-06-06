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
def solve(N, L, K, A):
    A = [0] + A + [L]
    A = [A[i + 1] - A[i] for i in range(N + 1)]

    def check(x):
        tmp = 0
        cnt = 0
        for a in A:
            tmp += a
            if tmp >= x:
                tmp = 0
                cnt += 1
                if cnt == K + 1:
                    return True
        tmp = 0
        cnt = 0
        for a in reversed(A):
            tmp += a
            if tmp >= x:
                tmp = 0
                cnt += 1
                if cnt == K + 1:
                    return True
        return False

    print(binary_search(1, L, check))


if __name__ == '__main__':
    N, L = map(int, input().split())
    K = int(input())
    A = [int(i) for i in input().split()]
    solve(N, L, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
