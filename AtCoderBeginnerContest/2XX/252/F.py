# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from heapq import heappush, heappop, heapify
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, L, A):
    cost = 0
    x = L - sum(A)
    B = A + ([x] if x > 0 else [])
    B.sort()
    while len(B) > 1:
        p, q = heappop(B), heappop(B)
        cost += p + q
        heappush(B, p + q)
    print(cost)


if __name__ == '__main__':
    N, L = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, L, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
