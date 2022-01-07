# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def prime_factorization(x):
    """素因数分解"""
    import math
    re = []
    i = 2
    while x != 1:
        if x % i == 0:
            re.append(i)
            x //= i
        else:
            i += 1
            if i > math.sqrt(x):
                re.append(x)
                break
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(A, B):
    primes = dict()
    for x in range(B + 1, A + 1):
        for p in prime_factorization(x):
            primes.setdefault(p, 0)
            primes[p] += 1
    ans = 1
    for p in primes.values():
        ans *= p + 1
        ans %= mod
    print(ans)


if __name__ == '__main__':
    A, B = map(int, input().split())
    solve(A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
