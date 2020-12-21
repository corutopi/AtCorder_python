"""
解説を参考に作成

s + k * x ≡ 0 mod n を解く(xを求める).
s, k, n を 最大公約数で割る(逆元を取るため).
式を変換して
    k * x ≡ (n - s) mod n
     -> k, n が互いに素でないなら(逆元が存在しないので) -1
n における k の逆元 k**-1 から、
    k * k**-1 ≡ 1 mod n
    k * k**-1 * (n - s) ≡ (n - s) mod n
よって x = k**-1 * (n - s) となり, これを求めればよい.

todo:
    baby-step giant-step というアルゴリズムを使う方法もあるらしい
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7


def gcd(a, b):
    """最大公約数"""
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    return gcd(b, a % b)


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
def solve(T, NSK):
    for n, s, k in NSK:
        a = k
        b = n - s
        m = n

        d = gcd(gcd(a, b), m)
        a = a // d
        b = b // d
        m = m // d
        if gcd(a, m) != 1:
            print(-1)
            continue
        print(inverse(a, m) * b % m)


if __name__ == '__main__':
    T = int(input())
    NSK = [[int(i) for i in input().split()] for _ in range(T)]
    solve(T, NSK)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
