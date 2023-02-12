# 解説などを参考に作成
# https://mathtrain.jp/hojo
# https://qiita.com/DaikiSuyama/items/4d0388a3f68b60c3e5f3
# https://atcoder.jp/contests/abc172/submissions/16541798
# tag: 包除原理
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque


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
    mod = 10 ** 9 + 7
    mPm = [1] + [i for i in range(1, M + 1)]
    for i in range(1, M + 1):
        mPm[i] = (mPm[i] * mPm[i - 1]) % mod
    ans = 0
    for j in range(0, N + 1):
        nCj = dev_mod(dev_mod(mPm[N], mPm[N - j], mod), mPm[j], mod)
        mPj = dev_mod(mPm[M], mPm[M - j], mod)
        mjPnj = dev_mod(mPm[M - j], mPm[(M - j) - (N - j)], mod)
        ans = (ans + nCj * (-1) ** j * mPj * mjPnj ** 2) % mod
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    solve(N, M)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
