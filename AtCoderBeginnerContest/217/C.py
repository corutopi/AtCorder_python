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
def solve(N, p):
    q = [0] * (N + 1)
    for i in range(N + 1):
        q[p[i]] = i
    print(" ".join([str(j) for j in q[1:]]))


if __name__ == '__main__':
    N = int(input())
    p = [int(i) for i in input().split()]
    p = [0] + p
    solve(N, p)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
