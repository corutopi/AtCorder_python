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
    D = divisor(N)

    def F(a, b):
        return max(len(str(a)), len(str(b)))

    ans = N
    for d in D[:len(D) // 2 + 1]:
        a, b = d, N // d
        ans = min(ans, F(a, b))
    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()

    # from tool.formath import divisor
    # print(divisor(10 ** 10))
