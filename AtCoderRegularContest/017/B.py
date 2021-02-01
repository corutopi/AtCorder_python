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
def solve(N, K, A):
    ans = 0
    up = 0
    now = 0
    for a in A:
        if now < a:
            up += 1
        else:
            up = 1
        if up >= K:
            ans += 1
        now = a
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(input()) for _ in range(N)]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
