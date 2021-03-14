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
def solve(N, f):
    group_count = 0
    visited = [0] * (N + 1)
    f = [0] + f
    g_num = 1
    for i in range(1, N + 1):
        if visited[i] > 0: continue
        visited[i] = g_num
        tmp = i
        while visited[f[tmp]] == 0:
            tmp = f[tmp]
            visited[tmp] = g_num
        if visited[f[tmp]] == g_num:
            group_count += 1
        g_num += 1
    print((pow(2, group_count, mod2) - 1) % mod2)


if __name__ == '__main__':
    N = int(input())
    f = [int(i) for i in input().split()]
    solve(N, f)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 2 * 10 ** 5
    # f = [i for i in range(1, N + 1)]
    # solve(N, f)
