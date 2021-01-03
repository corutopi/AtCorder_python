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
def solve(N):
    limit = 3500
    for h in range(1, limit + 1):
        for n in range(1, limit + 1):
            tmp = 4 * h * n - N * n - N * h
            if tmp <= 0:
                continue
            if N * h * n % tmp == 0:
                w = (N * h * n) // tmp
                print(h, n, w)
                return


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
