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
def solve(N, P, Q, AB):
    human = [0] * (N + 1)
    for i in range(N):
        human[P[i]] = i
    for a, b in AB:
        print(a if human[a] < human[b] else b)


if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]
    Q = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, P, Q, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
