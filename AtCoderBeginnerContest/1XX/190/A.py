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
def solve(A, B, C):
    if C == 0:
        if A > B:
            print('Takahashi')
        else:
            print('Aoki')
    else:
        if A >= B:
            print('Takahashi')
        else:
            print('Aoki')


if __name__ == '__main__':
    A, B, C = map(int, input().split())
    solve(A, B, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
