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
def solve(T, case):
    for c in case:
        if c % 2 == 1:
            print('Odd')
        elif c % 4 == 0:
            print('Even')
        else:
            print('Same')


if __name__ == '__main__':
    T = int(input())
    case = [int(input()) for _ in range(T)]
    solve(T, case)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
