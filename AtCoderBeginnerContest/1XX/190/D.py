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
def solve(N):
    ans = 0
    for x in range(1, N + 1):
        if x % 2 == 0:
            if N // x < x // 2:
                break
            if (N % x) * 2 == x:
                ans += 2
        else:
            if N // x - 1 < x // 2:
                break
            if N % x == 0:
                ans += 2
    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
