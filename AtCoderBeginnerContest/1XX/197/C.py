# import sys
# sys.setrecursionlimit(10 ** 6)
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
def solve(N, A):
    ans = 2 ** 30
    for i in range(2 ** N):
        a = 0
        b = 0
        for j in range(N):
            if i >> j & 1:
                a ^= b
                b = A[j]
            else:
                b |= A[j]
        a ^= b
        ans = min(ans, a)
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
    # N = 20
    # A = [2 ** 30 - 1 for _ in range(N)]
    # solve(N, A)
