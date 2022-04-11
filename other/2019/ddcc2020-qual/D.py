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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(M, DC):
    D = 0
    S = 0
    for d, c in DC:
        D += c
        S += d * c
    print(D - 1 + (S - 1) // 9)


if __name__ == '__main__':
    # S = input()
    M = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    DC = [[int(i) for i in input().split()] for _ in range(M)]
    # P = [int(input()) for _ in range(N)]
    solve(M, DC)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
