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
def solve(N, M, T):
    ans = 0
    for i, j in ((i, j) for i in range(N - 1) for j in range(i + 1, N)):
        ans += 1 if sum(T[i][k] | T[j][k] for k in range(M)) == M else 0
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    T = [[1 if i == 'o' else 0 for i in input()] for _ in range(N)]
    solve(N, M, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
