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
def solve(N, A):
    ans = 0

    def dfs(r, c, vr, vc, depth, now):
        if depth >= N:
            return now
        return dfs((r + vr) % N, (c + vc) % N,
                   vr, vc, depth + 1, now * 10 + int(A[r][c]))

    for i, j in ((i, j) for i in range(N) for j in range(N)):
        for q, p in ((-1, -1), (-1, 0), (-1, 1),
                     (0, -1), (0, 1),
                     (1, -1), (1, 0), (1, 1)):
            ans = max(ans, dfs(i, j, p, q, 0, 0))

    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [input() for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
