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
def solve(n):
    def solve(x):
        if (x * (x + 1)) // 2 <= n + 1:
            return True
        return False
    print(n - binary_search(1, n + 1, solve) + 1)


if __name__ == '__main__':
    n = int(input())
    solve(n)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
