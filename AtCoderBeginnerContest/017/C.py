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
def solve(N, M, LRS):
    LS = sorted([lrs[::2] for lrs in LRS])
    RS = sorted([lrs[1:] for lrs in LRS])
    all_remains = sum(lrs[-1] for lrs in LRS)
    jewel = 0
    ans = 0
    l = 0
    r = 0
    for i in range(1, M + 1):
        while l < N and LS[l][0] <= i:
            jewel += LS[l][1]
            l += 1
        ans = max(ans, all_remains - jewel)
        while r < N and RS[r][0] <= i:
            jewel -= RS[r][1]
            r += 1
    print(ans)


if __name__ == '__main__':
    N, M = map(int, input().split())
    LRS = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, M, LRS)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
