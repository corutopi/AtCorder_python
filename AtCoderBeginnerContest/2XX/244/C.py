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
def solve(N):
    called = [0] * (2 * N + 1 + 1)
    called[0] = 1
    aoki = 9999
    while aoki > 0:
        for i in range(1, 2 * N + 1 + 1):
            if called[i] == 0:
                print(i, flush=True)
                called[i] = 1
                break
        aoki = int(input())
        called[aoki] = 1


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
