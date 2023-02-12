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
def solve(N, S, D, XY):
    for x, y in XY:
        if x < S and y > D:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    N, S, D = map(int, input().split())
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, S, D, XY)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
