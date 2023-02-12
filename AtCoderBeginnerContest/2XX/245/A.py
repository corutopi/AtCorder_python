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
def solve(A, B, C, D):
    print('Takahashi' if A * 60 + B < C * 60 + D + 1 else 'Aoki')


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    A, B, C, D = map(int, input().split())
    solve(A, B, C, D)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
