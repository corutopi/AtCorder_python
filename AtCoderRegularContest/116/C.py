# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
# mod = 10 ** 9 + 7
mod2 = 998244353


def prime_factorization(x):
    """素因数分解"""
    import math
    re = {}
    i = 2
    while x != 1:
        if x % i == 0:
            re.setdefault(i, 0)
            re[i] += 1
            x //= i
        else:
            i += 1
            if i > math.sqrt(x):
                re.setdefault(x, 0)
                re[x] += 1
                break
    return re


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
def solve(N, M):
    f = [1, 1]
    for i in range(2, 3 * 10 ** 5 + 1):
        f.append((f[-1] * i) % mod2)

    ans = 0
    for i in range(1, M + 1):
        pf = prime_factorization(i)
        tmp = 1
        for v in pf.values():
            tmp *= dev_mod(dev_mod(f[N - 1 + v], f[N - 1], mod2), f[v], mod2)
            tmp %= mod2
        ans += tmp
        ans %= mod2
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    solve(N, M)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # for n, m in ((i, j) for i in range(1, 100) for j in range(1, 100)):
    #     solve(n, m)
