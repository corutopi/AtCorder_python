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
def solve(N, APX):
    ans = 10 ** 10
    for a, p, x in APX:
        if x > a:
            ans = min(ans, p)
    print(ans if ans < 10 ** 10 else -1)



if __name__ == '__main__':
    N = int(input())
    APX = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, APX)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
