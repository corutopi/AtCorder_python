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
def solve(N, P):
    table = [0] * N
    for i in range(N):
        table[P[i] - i if P[i] >= i else N + P[i] - i] += 1
    ans = 0
    for i in range(N):
        ans = max(ans, sum([table[i % N],
                            table[(i + 1) % N],
                            table[(i + 2) % N]]))
    print(ans)


if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]
    solve(N, P)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
