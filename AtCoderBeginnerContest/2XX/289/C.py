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
def solve(N, M, D):
    ans = 0
    for i in range(1, 2 ** M):
        tmp = 0
        for j in range(M):
            if i >> j & 1:
                tmp |= D[j]
        if tmp == 2 ** N - 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    D = []
    for _ in range(M):
        input()
        tmp = 0
        for s in input().split():
            tmp |= 1 << (int(s) - 1)
        D.append(tmp)
    solve(N, M, D)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
