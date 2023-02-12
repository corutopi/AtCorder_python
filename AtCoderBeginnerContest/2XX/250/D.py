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


def binary_search(ok, ng, solve):
    """めぐる式2分探索"""
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if solve(mid):
            ok = mid
        else:
            ng = mid
    return ok


def prime_numbers(m):
    """m以下の素数リスト"""
    re = []
    first_prime = [0] * (m + 1)
    if m <= 1:
        return re
    for i in range(2, m + 1):
        if first_prime[i] > 0:
            continue
        re.append(i)
        for j in range(i * i, m + 1, i):
            first_prime[j] = i
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    pn = [0] + prime_numbers(ceil(N ** (1 / 3)))
    ans = 0
    for q in pn[1:]:
        x = min(N // (q ** 3), q - 1)
        ans += binary_search(0, len(pn), lambda y: pn[y] <= x)
    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
