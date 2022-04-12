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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A, B, C, D):
    u_u = A
    u_b = A
    b_u = A
    b_b = A
    for i in range(N - 2):
        u_u += D
        u_b += C
        b_u -= C
        b_b -= D
        x = N - 2 - i
        if (u_b - D * x <= B <= u_u - C * x) or \
                (b_b + C * x <= B <= b_u + D * x):
            print('YES')
            return
    print('NO')


if __name__ == '__main__':
    N, A, B, C, D = map(int, input().split())
    solve(N, A, B, C, D)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
