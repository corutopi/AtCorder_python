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
def solve(N, M, A, C):
    B = [0] * (M + 1)

    for m in range(M, -1, -1):
        o = m + N
        c = C[o]
        for n in range(max(0, o - M), N):
            c -= A[n] * B[o - n]
        B[m] = c // A[N]
    print(*B)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    C = [int(i) for i in input().split()]
    solve(N, M, A, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
