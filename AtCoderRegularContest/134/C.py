# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def inverse(a, p):
    """逆元"""
    a_, p_ = a, p
    x, y = 1, 0
    while p_:
        t = a_ // p_
        a_ -= t * p_
        a_, p_ = p_, a_
        x -= t * y
        x, y = y, x
    x %= p
    return x


def dev_mod(a, b, mod):
    """a(= A % mod) / b を mod で割った余り"""
    return (a * inverse(b, mod)) % mod


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, a):
    if a[0] < K + sum(a[1:]):
        print(0)
        return
    a[0] -= K + sum(a[1:])
    base = 1
    for i in range(K - 1):
        base *= i + 1
        base %= mod2

    ans = 1
    for ai in a:
        t = 1
        for i in range(K - 1):
            t *= ai + i + 1
            t %= mod2
        ans *= dev_mod(t, base, mod2)
        ans %= mod2

    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    a = [int(i) for i in input().split()]
    solve(N, K, a)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 10 ** 5
    # K = 200
    # a = random_ints(N - 1, 1, mod2 // 2)
    # a = [sum(a) + K + randint(1, 100)] + a
    # solve(N, K, a)
