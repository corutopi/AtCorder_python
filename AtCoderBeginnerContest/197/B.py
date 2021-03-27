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
def solve(H, W, X, Y, S):
    S = ['#' * (W + 2)] + ['#' + s + '#' for s in S] + ['#' * (W + 2)]
    ans = 1
    i = 1
    while S[X - i][Y] == '.':
        i += 1
        ans += 1
    i = 1
    while S[X + i][Y] == '.':
        i += 1
        ans += 1
    i = 1
    while S[X][Y - i] == '.':
        i += 1
        ans += 1
    i = 1
    while S[X][Y + i] == '.':
        i += 1
        ans += 1
    print(ans)


if __name__ == '__main__':
    H, W, X, Y = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, X, Y, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
