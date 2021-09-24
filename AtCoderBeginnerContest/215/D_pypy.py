# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def divisor(x):
    """約数"""
    from math import floor
    re = []
    _x = floor(x ** 0.5)
    for i in range(1, _x + 1):
        if x % i == 0:
            re.append(i)
            if x // i != i:
                re.append(x // i)
    re.sort()
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, A):
    div_list = [0] * (max(A + [M]) + 1)
    ans = []
    for a in A:
        for x in divisor(a):
            div_list[x] = 1
    for k in range(1, M + 1):
        for y in divisor(k)[1:]:
            if div_list[y] == 1:
                break
        else:
            ans.append(k)
    print(len(ans))
    [print(a) for a in ans]


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, M, A)

    # # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, M = 10 ** 5, 10 ** 5
    # A = [randint(1, 10 ** 5) for _ in range(N)]
    # solve(N, M, A)
