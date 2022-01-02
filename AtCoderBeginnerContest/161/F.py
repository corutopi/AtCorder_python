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
def solve(N):
    # N % K = 1 の場合
    dvs = divisor(N - 1)[1:]
    # Kの約数で当てはまるものがある場合
    for d in divisor(N)[1:]:
        n = N
        while n % d == 0:
            n = n // d
        if n % d == 1:
            dvs.append(d)
    print(len(dvs))


def solve_force(N):
    ans = []
    for i in range(2, N + 1):
        n = N
        while n % i == 0:
            n = n // i
        if n % i == 1:
            ans.append(i)
    print(*ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)
    # solve_force(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
