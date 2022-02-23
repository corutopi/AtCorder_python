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
def solve(N, xyc):
    ans = 0
    for i, j in ((i, j) for i in range(N - 1) for j in range(i + 1, N)):
        xi, yi, ci = xyc[i]
        xj, yj, cj = xyc[j]
        ans = max(ans, abs(xi - xj) * cj / (ci + cj) * ci)
        ans = max(ans, abs(yi - yj) * cj / (ci + cj) * ci)
    print(ans)


if __name__ == '__main__':
    N = int(input())
    xyc = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, xyc)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
