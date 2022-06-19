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
def solve(N):
    tmp = []
    for i in range(N):
        tmp.append([i * N + j for j in range(1, N + 1)])
    for i in range(N // 2):
        print(*tmp[i])
        print(*tmp[N // 2 + N % 2 + i])
    if N % 2 == 1:
        print(*tmp[N // 2])


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
