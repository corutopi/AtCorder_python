# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from heapq import heappush, heappop
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
def solve(N, A):
    A = sorted([-a for a in A])
    ans = 0
    x = A.pop() * -1
    while len(A) > 0:
        ans += 1
        y = (- heappop(A)) % x
        if y == 0:
            continue
        x, y = min(x, y), max(x, y)
        heappush(A, -y)
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2 * 10 ** 5
    # # A = random_ints(N, 1, 10 ** 9)
    # A = [1134903170] * (N // 2) + [701408733] * (N // 2)
    # solve(N, A)

# a, b = 0, 1
# for i in range(50):
#     a, b = a + b, a
#     if a > 10 ** 9:
#         print(a, b)
#         break
