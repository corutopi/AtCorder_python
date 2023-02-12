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
def solve(N, C):
    C.sort()
    ans = C[0]
    for i in range(1, N):
        ans *= C[i] - i
        if ans <= 0:
            print(0)
            return
        ans %= mod
    print(ans)


if __name__ == '__main__':
    N = int(input())
    C = [int(i) for i in input().split()]
    solve(N, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
