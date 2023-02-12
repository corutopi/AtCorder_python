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
def solve(S1, S2, S3):
    l = ['ABC', 'ARC', 'AGC', 'AHC']
    l.remove(S1)
    l.remove(S2)
    l.remove(S3)
    print(l[0])


if __name__ == '__main__':
    S1 = input()
    S2 = input()
    S3 = input()
    solve(S1, S2, S3)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
