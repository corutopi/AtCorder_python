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
def solve(V, T, S, D):
    print('No' if T * V <= D <= S * V else 'Yes')


if __name__ == '__main__':
    V, T, S, D = map(int, input().split())
    solve(V, T, S, D)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
