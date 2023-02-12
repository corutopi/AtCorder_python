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
def solve(N, c):
    pattern = ['A', 'B', 'X', 'Y']
    pattern = [p1 + p2 for p1 in pattern for p2 in pattern]
    ge = ((L, R) for L in pattern for R in pattern)

    ans = N
    for L, R in ge:
        tmp = c
        ans = min(len(tmp.replace(L, 'L').replace(R, 'R')), ans)

    print(ans)


if __name__ == '__main__':
    N = int(input())
    c = input()
    solve(N, c)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 1000
    # c = random_str(N, 'ABXY')
    # solve(N, c)
