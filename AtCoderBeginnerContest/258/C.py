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
def solve(N, Q, S, query):
    start = 0
    for n, x in query:
        if n == 1:
            start -= x
        else:
            print(S[(x - 1 + start) % N])


if __name__ == '__main__':
    N, Q = map(int, input().split())
    S = input()
    query = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, S, query)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
