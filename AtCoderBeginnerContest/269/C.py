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
def solve(N):
    LIMIT = 60
    b1_list = []
    for i in range(LIMIT):
        if N >> i & 1:
            b1_list.append(i)
    for j in range(2 ** len(b1_list)):
        ans = 0
        for k in range(len(b1_list)):
            ans += 2 ** b1_list[k] if j >> k & 1 else 0
        print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
