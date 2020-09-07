# 解説を参考に作成
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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(n, k):
    mod = 10 ** 9 + 7
    ans = 0
    p_mod = [1, 1]
    for i in range(2, n + 1):
        p_mod.append((p_mod[-1] * i) % mod)

    for i in range(min(n, k + 1)):
        if i == 0:
            ans += 1
        elif i == 1:
            ans += n * (n - 1)
        else:
            nCi = p_mod[n] * inverse(p_mod[n - i], mod) % mod * inverse(p_mod[i], mod) % mod
            nmHi = (p_mod[n - 1] * inverse(p_mod[n - i - 1], mod) % mod) * inverse(p_mod[i], mod) % mod
            # ans += cmb2(n, i, mod) * cmb2(n - 1, i, mod)
            ans += nCi * nmHi % mod
        ans %= mod
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    n, k = map(int, input().split())
    # Ai = [int(i) for i in input().split()]
    # Bi = [int(i) for i in input().split()]
    # ABi = [[int(i) for i in input().split()] for _ in range(N)]
    solve(n, k)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
