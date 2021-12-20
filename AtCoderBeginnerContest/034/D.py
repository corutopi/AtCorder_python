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


def binary_search_double(ok, ng, solve, cnt=100):
    """めぐる式2分探索"""
    for _ in range(cnt):
        mid = (ok + ng) / 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, wp):
    def solver(x):
        tmp = []
        for w, p in wp:
            tmp.append((w * p / 100) - (w * x / 100))
        tmp.sort(reverse=True)
        return sum(tmp[:K]) >= 0

    print(binary_search_double(0, 101, solver))


if __name__ == '__main__':
    N, K = map(int, input().split())
    wp = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, wp)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
