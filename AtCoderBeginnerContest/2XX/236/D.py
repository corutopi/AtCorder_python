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
def solve(N, A):
    member = [i for i in range(2 * N)]

    def dfs(n, m):
        x = m[0]
        r = 0
        if len(m) == 2:
            return n ^ A[x][m[1] - x - 1]
        else:
            for i in range(1, len(m)):
                r = max(r, dfs(n ^ A[x][m[i] - x - 1], m[1:i] + m[i + 1:]))
            return r

    print(dfs(0, member))


if __name__ == '__main__':
    N = int(input())
    A = [[int(i) for i in input().split()] for _ in range(2 * N - 1)]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 8
    # A = [random_ints(2 * N - 1 - j, 0, 2 ** 30) for j in range(2 * N - 1)]
    # solve(N, A)
