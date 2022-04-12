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
def solve(N, A):
    A.sort()
    if A[-1] - A[0] > 1:
        print('No')
    elif A[-1] == A[0]:
        print('Yes' if A[0] == N - 1 or N // A[0] >= 2 else 'No')
    else:
        x = sum(1 if A[i] == A[0] else 0 for i in range(N))
        print('Yes' if A[-1] - x != 0 and (N - x) // (A[-1] - x) >= 2 else 'No')


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
