# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def gcd(a, b):
    """最大公約数"""
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, X):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    ans = inf
    for i in range(2 ** 15):
        tmp = 1
        for j in range(15):
            tmp *= primes[j] if i >> j & 1 else 1
        flg = True
        for x in X:
            if gcd(tmp, x) == 1:
                flg = False
                break
        if flg:
            ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    N = int(input())
    X = [int(i) for i in input().split()]
    solve(N, X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 50
    # X = [randint(2, 50) for _ in range(N)]
    # solve(N, X)
