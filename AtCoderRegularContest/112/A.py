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
def solve(T, case):
    for L, R in case:
        if L * 2 > R:
            print(0)
            continue
        key = R - L * 2 + 1
        print((key * (key + 1)) // 2)


if __name__ == '__main__':
    T = int(input())
    case = [[int(i) for i in input().split()] for _ in range(T)]
    solve(T, case)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
