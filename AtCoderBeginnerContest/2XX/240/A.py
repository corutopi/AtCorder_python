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
def solve(a, b):
    print('Yes' if abs(a % 10 - b % 10) == 1 or abs(a - b) == 1 else 'No')


if __name__ == '__main__':
    a, b = map(int, input().split())
    solve(a, b )

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
