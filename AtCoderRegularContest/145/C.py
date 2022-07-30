"""
解説AC
カタラン数
"""
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


class FermatCmb:
    """フェルマー小定理を使用した順列, 組み合わせ計算
    max_num = 10 ** 6 で 0.58 sec
    """

    def __init__(self, max_num, mod):
        """
        :param max_num: max n of nCk
        :param mod: any prime number
        """
        self.max_num = max_num
        self.mod = mod
        self.fact = [0 for _ in range(max_num + 1)]
        self.factinv = [0 for _ in range(max_num + 1)]

        self.fact[0] = 1
        for i in range(1, max_num + 1):
            self.fact[i] = (i * self.fact[i - 1]) % self.mod

        self.factinv[-1] = pow(self.fact[-1], mod - 2, mod)
        for i in range(max_num, 0, -1):
            self.factinv[i - 1] = self.factinv[i] * i
            self.factinv[i - 1] %= self.mod

    def nCk(self, n, k):
        return (self.fact[n] * self.factinv[k] * self.factinv[n - k]) % self.mod

    def nPk(self, n, k):
        return (self.fact[n] * self.factinv[n - k]) % self.mod


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
def solve(N):
    fc = FermatCmb(N * 2, mod2)
    ans = fc.nPk(N * 2, N * 2)
    ans = dev_mod(ans, fc.nPk(N + 1, N + 1), mod2)
    ans = ans * pow(2, N, mod2)
    print(ans % mod2)


def solve_support(N):
    x = [i + 1 for i in range(N)]

if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
