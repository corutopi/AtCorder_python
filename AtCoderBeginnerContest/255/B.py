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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A, XY):
    ans = [inf] * N
    for i in range(N):
        x, y = XY[i]
        for a in A:
            n, m = XY[a - 1]
            ans[i] = min(ans[i], (abs(x - n) ** 2 + abs(y - m) ** 2) ** 0.5)
    print(max(ans))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    XY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, K, A, XY)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
