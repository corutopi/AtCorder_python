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
def solve(N, T):
    x, y = 0, 0
    now = 'E'
    for t in T:
        if t == 'S':
            if now == 'E':
                x += 1
            elif now == 'S':
                y -= 1
            elif now == 'W':
                x -= 1
            elif now == 'N':
                y += 1
        else:
            if now == 'E':
                now = 'S'
            elif now == 'S':
                now = 'W'
            elif now == 'W':
                now = 'N'
            elif now == 'N':
                now = 'E'
    print(x, y)


if __name__ == '__main__':
    N = int(input())
    T = input()
    solve(N, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
