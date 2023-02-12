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
def solve(N):
    def solver(x, y, win):
        if y <= 1 <= x:
            print('Aoki' if win else 'Takahashi')
            return
        if win:
            solver(y - 1, y // 2, False)
        else:
            solver(y - 1, y // 2 + y % 2, True)

    solver(inf, N + 1, False)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
