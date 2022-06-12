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
def solve(N, Q, A, X):
    A.append(0)
    A.sort()
    cumsum_A = [0]
    for a in A:
        cumsum_A.append(cumsum_A[-1] + a)

    for x in X:
        tmp = binary_search(0, N + 1, lambda l: A[l] <= x)
        print(abs(cumsum_A[tmp + 1] - x * (tmp + 1)) +
              abs(cumsum_A[-1] - cumsum_A[tmp + 1] - x * (N - tmp)) - x)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, Q = map(int, input().split())
    A = [int(i) for i in input().split()]
    X = [int(input()) for _ in range(Q)]
    solve(N, Q, A, X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
