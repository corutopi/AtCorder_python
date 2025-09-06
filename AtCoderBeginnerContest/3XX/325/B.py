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
def solve(N ,WX):
    ans_member = 0
    for i in range(24):
        # print(i, ':', [w for w, x in WX if 9 <= (x + i) % 24 <= 17])
        ans_member = max(ans_member, sum(w for w, x in WX if 9 <= (x + i) % 24 <= 17))
    print(ans_member)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    WX = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(N ,WX)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
