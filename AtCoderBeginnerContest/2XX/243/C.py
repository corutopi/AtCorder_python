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
def solve(N, XY, S):
    lr_dict = dict()
    for i in range(N):
        x, y = XY[i]
        s = S[i]
        lr_dict.setdefault(y, {'L': -inf, 'R': inf})
        if s == 'L':
            lr_dict[y][s] = max(lr_dict[y][s], x)
        else:
            lr_dict[y][s] = min(lr_dict[y][s], x)
    for v in lr_dict.values():
        if v['L'] > v['R']:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    N = int(input())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    S = input()
    solve(N, XY, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
