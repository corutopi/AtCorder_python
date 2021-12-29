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
def solve(N, A, B, h):
    def solver(x):
        hp = [max(0, y - B * x) for y in h]
        hp = [y // (A - B) + bool(y % (A - B)) for y in hp]
        return sum(hp) <= x

    print(binary_search(10 ** 9, 0, solver))


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    h = [int(input()) for _ in range(N)]
    solve(N, A, B, h)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 10 ** 5
    # B = randint(1, 10 ** 9 - 1)
    # A = randint(B + 1, 10 ** 9)
    # h = [randint(1, 10 ** 9) for _ in range(N)]
    # solve(N, A, B, h)
