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

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7


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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(K):
    primes = prime_factorization_dict(K)
    ans = 0
    for k, v in primes.items():
        tmp = 0
        for i in range(1, v + 1):
            tmp += 1
            now = i
            while now % k == 0:
                tmp += 1
                now //= k
            if v <= tmp:
                ans = max(ans, k * i)
                break
    print(ans)



if __name__ == '__main__':
    K = int(input())
    solve(K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
