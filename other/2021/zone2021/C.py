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
def solve(N, ABCDE):
    def solver(x):
        bin_ABCDE = set()
        for abcde in ABCDE:
            t = 0
            for p in abcde:
                t <<= 1
                t += 1 if x <= p else 0
            bin_ABCDE.add(t)
        bin_ABCDE = list(bin_ABCDE) + [0, 0]
        lng = len(bin_ABCDE)
        for l, m, n in ((l, m, n)
                        for l in range(lng - 2)
                        for m in range(l + 1, lng - 1)
                        for n in range(m + 1, lng)):
            if bin_ABCDE[l] | bin_ABCDE[m] | bin_ABCDE[n] == 31:
                return True
        else:
            return False

    print(binary_search(0, 10 ** 9 + 1, solver))


if __name__ == '__main__':
    N = int(input())
    ABCDE = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, ABCDE)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 3000
    # ABCDE = [random_ints(5, 1, 10 ** 9) for _ in range(N)]
    # solve(N, ABCDE)
