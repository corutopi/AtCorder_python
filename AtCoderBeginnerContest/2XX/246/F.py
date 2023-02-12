"""
解説AC
包除原理
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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, L, S):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    alp_dict = {alp[x]: x for x in range(len(alp))}
    sint = [sum([1 << alp_dict[c] for c in s]) for s in S]
    ans = 0
    for i in range(1, 1 << N):
        vector = -1
        target = (1 << len(alp)) - 1
        for j in range(N):
            if i >> j & 1:
                target &= sint[j]
                vector *= -1
        ans += pow(sum((target >> x & 1 for x in range(len(alp)))), L,
                   mod2) * vector
        ans %= mod2
    print(ans)


if __name__ == '__main__':
    N, L = map(int, input().split())
    S = [input() for _ in range(N)]
    solve(N, L, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
