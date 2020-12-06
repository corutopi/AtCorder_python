# 解説を参考に作成
"""
S = sum(A)
とすると、nCm(n=N + M, m=N + S) で答えとなる.
例：
3 5
1 2 1
の入力の場合, nCm(n=8, m=7) となる.
これをn個の●の内、m個を○で塗りつぶすと考える.
  ○○○○○○○●
  ○●○○○○○○
  ○○○○●○○○
  …
これを○だけで数えて先頭から各 ΣAi(i=x) + x 番目の○を｜に変えると
  ○｜○○｜○｜●
  ○●｜○○｜○｜
  ○｜○○●｜○｜
  …
のようになる.
｜をしきりとして左から
  1~i番目: ○,● の合計がBi, ○の位置がBiからAiを選ぶパターン
  i+1番目: sum(Bi) < M となる場合の、M - sum(Bi)
を表現しているものとして読み取ることができる.
よってこれで条件に合うすべてのパターンを網羅できていることになる.
"""


# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque

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
def solve(N, M, A):
    S = sum(A)
    print(cmb2(N + M, N + S, 10 ** 9 + 7))


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, M, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    #
    # N, M = 2000, randint(1, 10 ** 9)
    # A = [randint(2000, 2000) for _ in range(N)]
    # solve(N, M, A)
