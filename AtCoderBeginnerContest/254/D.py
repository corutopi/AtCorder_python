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


def prime_factorization_dict(x):
    """素因数分解
    return such as
        {f1: f1_num, f2: f2_num, ... , fn: fn_num}
    """
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


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    square = []
    i = 1
    while i ** 2 <= N:
        square.append(i ** 2)
        i += 1
    ans = len(square)
    for j in range(2, N + 1):
        x = prime_factorization_dict(j)
        t = 1
        for k, v in x.items():
            t *= k if v % 2 == 1 else 1
        ans += binary_search(0, len(square), lambda l: square[l] * t <= N) + 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    # N = 2 * 10 ** 5
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
