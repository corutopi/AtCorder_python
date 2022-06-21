"""
解説AC
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


def divisor(x):
    """約数"""
    from math import floor
    re = []
    _x = floor(x ** 0.5)
    for i in range(1, _x + 1):
        if x % i == 0:
            re.append(i)
            if x // i != i:
                re.append(x // i)
    re.sort()
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A):
    S = sum(A)
    D = divisor(S)
    ans = 0
    for d in D:
        R = sorted([a % d for a in A])
        sum_R = sum(R)
        minus = 0
        for i in range(N):
            minus += R[i]
            plus = d * (N - (i + 1)) - (sum_R - minus)
            if (minus == plus or abs(minus - plus) % d == 0) \
                    and max(minus, plus) <= K:
                ans = d
                break
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
