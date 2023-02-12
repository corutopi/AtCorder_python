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
def solve(H,W,R,C):

    print((0 if H == 1 else 2 if 1 < R < H else 1) +
          (0 if W == 1 else 2 if 1 < C < W else 1))


if __name__ == '__main__':
    H, W = map(int, input().split())
    R, C = map(int, input().split())
    solve(H,W,R,C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
