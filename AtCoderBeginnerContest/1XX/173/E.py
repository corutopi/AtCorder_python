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
def solve(N, K, As):
    mod = 10 ** 9 + 7
    As.sort()
    ans = 1
    if N == K:
        for a in As:
            ans = (ans * a) % mod
    elif As[-1] < 0 and K % 2 == 1:
        for k in range(1, K + 1):
            ans = (ans * As[- k]) % mod
    else:
        As.sort(key=abs)
        last_p = -1
        last_m = -1
        cnt_m = 0
        for k in range(1, K + 1):
            ans = (ans *  As[- k]) % mod
            if As[- k] < 0:
                last_m = As[- k]
                cnt_m += 1
            else:
                last_p = As[- k]
        if cnt_m % 2 == 1:
            mlt_p = max(As[:N - K])
            mlt_m = min(As[:N - K])
            if last_p < 0:
                ans = dev_mod(ans, last_m, mod) * mlt_p % mod
            elif mlt_m >= 0:
                ans = dev_mod(ans, last_m, mod) * mlt_p % mod
            elif mlt_p < 0:
                ans = dev_mod(ans, last_p, mod) * mlt_m % mod
            else:
                if abs(last_p * mlt_p) <= abs(last_m * mlt_m):
                    ans = dev_mod(ans, last_p, mod) * mlt_m % mod
                else:
                    ans = dev_mod(ans, last_m, mod) * mlt_p % mod
    print(ans % mod)


# def solve2(N, K, As):
#     mod = 10 ** 9 + 7
#     As.sort()
#     ans = 1
#     if N == K:
#         for a in As:
#             ans *= a
#     elif As[-1] < 0 and K % 2 == 1:
#         for k in range(1, K + 1):
#             ans *= As[- k]
#     else:
#         As.sort(key=abs)
#         last_p = None
#         last_m = None
#         cnt_m = 0
#         for k in range(1, K + 1):
#             ans *= As[- k]
#             if As[- k] < 0:
#                 last_m = As[- k]
#                 cnt_m += 1
#             else:
#                 last_p = As[- k]
#         if cnt_m % 2 == 1:
#             ans1 = ans // last_m * max(As[:N - K])
#             ans2 = ans // last_p * min(As[:N - K]) if last_p is not None else -1
#             ans = max(ans1, ans2)
#     print(ans % mod)


if __name__ == '__main__':
    N, K = map(int, input().split())
    As = [int(i) for i in input().split()]
    # import random
    # N, K = 2 * 10 ** 5, 10 ** 5
    # As = [random.randint(- 10 ** 9, 10 ** 9) for _ in range(N)]
    solve(N, K, As)
    # solve2(N, K, As)
