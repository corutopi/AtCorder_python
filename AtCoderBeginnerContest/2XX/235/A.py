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
def solve(abc):
    a, b, c = map(int, abc)
    print((a * 100 + b * 10 + c) +
          (b * 100 + c * 10 + a) +
          (c * 100 + a * 10 + b))


if __name__ == '__main__':
    abc = input()
    solve(abc)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
