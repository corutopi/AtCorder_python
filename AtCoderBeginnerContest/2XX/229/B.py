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
def solve(A, B):
    A, B = max(A, B), min(A, B)
    while A > 0:
        A, a = divmod(A, 10)
        B, b = divmod(B, 10)
        if a + b >= 10:
            print('Hard')
            return
    print('Easy')


if __name__ == '__main__':
    A, B = map(int, input().split())
    solve(A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
