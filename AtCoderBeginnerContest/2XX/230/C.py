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
def solve(N, A, B, P, Q, R, S):
    for i in range(P, Q + 1):
        print(''.join(['#' if abs(A - i) == abs(B - j) else '.' for j in
                       range(R, S + 1)]))
    pass


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    solve(N, A, B, P, Q, R, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
