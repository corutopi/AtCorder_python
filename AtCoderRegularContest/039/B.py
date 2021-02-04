# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def cmb2(n, r, mod):
    """組み合わせ(余り)"""

    if n < r:
        return 0
    re = 1
    for i in range(n - r + 1, n + 1):
        re = (re * i) % mod
    for i in range(1, r + 1):
        re = (re * inverse(i, mod)) % mod
    return re % mod


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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K):
    from math import factorial
    if N > K:
        print((factorial(N - 1 + K) // factorial(N - 1) // factorial(K)) % mod)
    else:
        print(cmb2(N, K % N, mod))


if __name__ == '__main__':
    N, K = map(int, input().split())
    solve(N, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
