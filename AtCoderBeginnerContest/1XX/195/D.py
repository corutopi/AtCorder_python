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
def solve(N, M, Q, WV, X, Query):
    WV.sort(key=lambda y: y[1], reverse=True)

    for l, r in Query:
        ans = 0
        x = sorted(X[:l - 1] + X[r:])

        for w, v in WV:
            if len(x) == 0: break
            if x[-1] < w: continue
            t = binary_search(len(x) - 1, -1, lambda y: w <= x[y])
            ans += v
            x = x[:t] + x[t + 1:]
        print(ans)


if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    WV = [[int(i) for i in input().split()] for _ in range(N)]
    X = [int(i) for i in input().split()]
    Query = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, M, Q, WV, X, Query)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, M, Q = 50, 10, 50
    # WV = [[randint(1, 10 ** 6) for _ in range(2)] for _ in range(N)]
    # X = [randint(1, 10 ** 6) for _ in range(M)]
    # Query = [sorted([randint(1, M) for _ in range(2)]) for _ in range(Q)]
    # solve(N, M, Q, WV, X, Query)
