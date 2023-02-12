# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, Q, ABCD):
    for a, b, c, d in ABCD:
        print(small_solver(M, a, b, c, d) % mod2)


def small_solver(M, a, b, c, d):
    row_num = b - a + 1
    col_num = d - c + 1

    x = M * (((a + b - 2) * row_num) // 2) * col_num
    y = row_num * ((c + d) * col_num) // 2
    tmp = x + y
    ans = 0
    if row_num % 2 == 0:
        if col_num % 2 == 0:
            ans = tmp // 2
        elif (a + c) % 2 == 1:
            ans = tmp // 2 + (1 if tmp % 2 == 1 else 0) \
                  + (row_num // 2 * M // 2)
        else:
            ans = tmp // 2 - (row_num // 2 * M // 2)
    elif col_num % 2 == 0:
        if (a + c) % 2 == 1:
            ans = tmp // 2 + (1 if tmp % 2 == 1 else 0) \
                  + col_num // 2 // 2
        else:
            ans = tmp // 2 - col_num // 2 // 2
    else:
        sa = (1 if (a + c) % 2 == 1 else -1) * (row_num - 1) // 2 * M
        sa += ((b - 1) * M + d - (col_num - 1) // 2) if (b + c) % 2 == 0 \
            else ((col_num - 1) // 2 - ((b - 1) * M + d))
        if sa > 0:
            ans = tmp // 2 + (1 if tmp % 2 == 1 else 0) \
                  + sa // 2
        else:
            ans = tmp // 2 - abs(sa) // 2
    return ans


def small_solver_force(M, a, b, c, d):
    ans = 0
    for i, j in ((i, j) for i in range(a, b + 1) for j in range(c, d + 1)):
        if (i + j) % 2 == 1: continue
        ans += (i - 1) * M + j
    return ans


if __name__ == '__main__':
    N, M = map(int, input().split())
    Q = int(input())
    ABCD = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, M, Q, ABCD)

    # for a, b, c, d in ABCD:
    #     if small_solver(M, a, b, c, d) != small_solver_force(M, a, b, c, d):
    #         print(M, a, b, c, d)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N, M = 10 ** 9, 10 ** 9
    # Q = 10 ** 5
    # ABCD = []
    # for _ in range(Q):
    #     a = randint(1, N)
    #     b = randint(a, N)
    #     c = randint(1, N)
    #     d = randint(c, N)
    #     ABCD.append([a, b, c, d])
    # solve(N, M, Q, ABCD)
