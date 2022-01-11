# import sys
# sys.setrecursionlimit(10 ** 6)
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
def solve(t):
    def f(x):
        return x ** 2 + 2 * x + 3

    print(f(f(f(t) + t) + f(f(t))))


if __name__ == '__main__':
    t = int(input())
    solve(t)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
