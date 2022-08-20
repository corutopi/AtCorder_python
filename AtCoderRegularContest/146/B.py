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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, K, A):
    n_2 = [2 ** i for i in range(32)]

    ans = 0
    B = A
    point = M
    for i in range(30, -1, -1):
        B_new = []
        cnt_1 = 0
        for b in B:
            x = b & (n_2[i + 1] - 1)
            B_new.append(x)
            cnt_1 += 1 if x >= n_2[i] else 0
        B_new.sort(reverse=True)
        tmp = sum(0 if b >= n_2[i] else n_2[i] - b for b in B_new[:K])
        if point >= tmp:
            ans += n_2[i]
            point -= tmp
            B_new = B_new[:cnt_1]
            B_new += [0] * (K - cnt_1) if K > cnt_1 else []
        B = B_new
    print(ans)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, M, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2 * 10 ** 5
    # K = 10 ** 5
    # M = randint(0, 2 ** 30)
    # A = random_ints(N, 0, 2 ** 30)
    # solve(N, M, K, A)
