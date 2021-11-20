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
def solve(N, K, P):
    Psum = [sum(p) for p in P]
    Psort = sorted(Psum) + [1201]
    for ps in Psum:
        print('Yes'
              if N - binary_search(0, N, lambda x: Psort[x] <= ps + 300) <= K
              else 'No')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, K = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    P = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, P)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
