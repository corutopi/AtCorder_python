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
def solve(N, H):
    ans = 0
    for h in H:
        if ans < h:
            ans = h
        else:
            break
    print(ans)


if __name__ == '__main__':
    N = int(input())
    H = [int(i) for i in input().split()]
    solve(N, H)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
