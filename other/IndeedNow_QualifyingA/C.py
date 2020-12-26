# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7


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
def solve(N, s, Q, k):
    shin_N = 0
    max_point = max(s)
    tokuten = [0] * (max_point + 1)
    for si in s:
        if si == 0:
            continue
        tokuten[si] += 1
        shin_N += 1
    border_sum = []
    border_sum.append(shin_N)
    for t in tokuten:
        border_sum.append(border_sum[-1] - t)

    for ki in k:
        if ki >= shin_N:
            print(0)
            continue
        print(binary_search(max_point + 1, 0, lambda x: border_sum[x] <= ki))


if __name__ == '__main__':
    N = int(input())
    s = [int(input()) for _ in range(N)]
    Q = int(input())
    k = [int(input()) for _ in range(Q)]
    solve(N, s, Q, k)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 10 ** 5
    # s = [randint(0, 10 ** 6) for _ in range(N)]
    # Q = 10 ** 5
    # k = [randint(0, N) for _ in range(Q)]
    # solve(N, s, Q, k)
