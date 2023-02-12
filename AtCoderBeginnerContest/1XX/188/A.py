# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(X, Y):
    win = max(X, Y)
    lose = min(X, Y) + 3
    print('Yes' if lose > win else 'No')


if __name__ == '__main__':
    X, Y = map(int, input().split())
    solve(X, Y)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
