# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
import string
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
def solve(N, S, Q, CD):
    ans = ""
    alpmap = {a: a for a in string.ascii_lowercase}
    for c, d in CD:
        for a in alpmap.keys():
            if alpmap[a] == c:
                alpmap[a] = d
    print("".join(alpmap[s] for s in S))


if __name__ == '__main__':
    N = int(input())
    S = input()
    Q = int(input())
    CD = [[s for s in input().split()] for _ in range(Q)]
    solve(N, S, Q, CD)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
