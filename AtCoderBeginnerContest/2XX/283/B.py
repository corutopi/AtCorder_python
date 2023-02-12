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
def solve(N, A, Q, query):
    for q in query:
        if q[0] == 1:
            A[q[1] - 1] = q[2]
        elif q[0] == 2:
            print(A[q[1] - 1])


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    Q = int(input())
    query = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, A, Q, query)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
