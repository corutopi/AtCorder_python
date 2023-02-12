# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from heapq import heappush, heappop
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
# def solve2(N, K, A):
#     A.sort(reverse=True)
#     hq = [0] * K
#     for a in A:
#         x = heappop(hq)
#         heappush(hq, x + a)
#     print(heappop(hq))
#     # return heappop(hq)


def solve(N, K, A):
    def solver(x):
        return x * K <= sum([min(a, x) for a in A])

    print(binary_search(1, 10 ** 20, solver))
    # return binary_search(1, 10 ** 20, solver)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints

    # N = 5
    # while True:
    #     K = randint(1, N)
    #     A = random_ints(N, 1, 5)
    #     if solve(N, K, A) != solve2(N, K, A):
    #         print(N, K)
    #         print(A)
    #         print(solve(N, K, A), solve2(N, K, A))
    #         break
