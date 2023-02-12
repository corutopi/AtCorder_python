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
def solve(H, W, N, AB):
    A = [0] + sorted(list(set([ab[0] for ab in AB])))
    B = [0] + sorted(list(set([ab[1] for ab in AB])))
    for a, b in AB:
        print(binary_search(0, len(A), lambda x: A[x] < a) + 1,
              binary_search(0, len(B), lambda x: B[x] < b) + 1)
        pass


if __name__ == '__main__':
    H, W, N = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(H, W, N, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # H, W, N = 10 ** 9,10 ** 9,10 ** 5
    # AB = [[randint(1, H), randint(1, W)] for _ in range(N)]
    # solve(H, W, N, AB)

