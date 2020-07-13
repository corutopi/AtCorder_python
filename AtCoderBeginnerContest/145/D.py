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


def dev_mod(a, b, mod):
    """a(= A % mod) / b を mod で割った余り"""
    return (a * inverse(b, mod)) % mod


# from decorator import stop_watch
#
#
# @stop_watch
def solve(X, Y):
    mod = 10 ** 9 + 7
    if (2 * Y - X) % 3 != 0:
        print(0)
        return
    a = round((2 * Y - X) / 3)
    b = Y - 2 * a
    a, b = max(a, b), min(a, b)

    if b < 0:
        print(0)
        return

    ans = 1
    for i in range(a + 1, a + b + 1):
        ans *= i
        ans %= mod
    ans %= mod
    for i in range(1, b + 1):
        ans = dev_mod(ans, i, mod)
    ans %= mod

    print(ans)


if __name__ == '__main__':
    X, Y = map(int, input().split())
    solve(X, Y)
