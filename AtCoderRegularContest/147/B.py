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

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7


def coordinate_compression(x, start=0):
    """整数のリストを座標圧縮したものを返す.デフォルトの最小値0.

    :param x: integer list
    :param start:
    :return:
    """
    xd = {v: i + start for i, v in enumerate(sorted(x))}
    return list(map(lambda d: xd[d], x))


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, P):
    P = coordinate_compression(P, 0)
    ans = []
    for i in range(2, N):
        t = i
        b = i % 2
        if P[t] % 2 != b:
            continue
        while t > b:
            if P[t - 2] % 2 == b:
                break
            P[t - 2], P[t] = P[t], P[t - 2]
            ans.append(['B', t - 2 + 1])
            t -= 2

    for i in range(N - 1):
        if P[i] % 2 != i % 2 and P[i + 1] % 2 != (i + 1) % 2:
            P[i], P[i + 1] = P[i + 1], P[i]
            ans.append(['A', i + 1])

    for i in range(2, N):
        t = i
        b = i % 2
        while t > b:
            if P[t - 2] > P[t]:
                P[t - 2], P[t] = P[t], P[t - 2]
                ans.append(['B', t - 2 + 1])
                t -= 2
            else:
                break

    print(len(ans))
    [print(*a) for a in ans]
    return ans, P


if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]
    solve(N, P)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # while True:
    #     N = randint(5, 10)
    #     P = random_ints(N, 1, 20, False)
    #     a, x = solve(N, P)
    #     for i in range(N - 1):
    #         if x[i] > x[i + 1]:
    #             print(P)
    #             print(a)
    #             print(x)
    #             break
    #     else:
    #         continue
    #     break
