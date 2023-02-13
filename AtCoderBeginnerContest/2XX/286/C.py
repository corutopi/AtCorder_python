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
def solve(N, A, B, S):
    ans = inf
    for i in range(N):
        ans = min(ans, A * i + B * sum(
            1 if S[x] != S[N - x - 1] else 0 for x in range(N // 2)))
        S = S[1:] + S[0]
    print(ans)


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    S = input()
    solve(N, A, B, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
