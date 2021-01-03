"""
解説を参考に作成
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
import itertools
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

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
    ans = []
    pn = prime_numbers(55555)
    pn = pn[1:]
    p = 0
    p4 = []
    while len(ans) < N:
        if pn[p] % 5 == 1:
            ans.append(pn[p])
        p += 1
    print(' '.join([str(i) for i in ans]))


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
