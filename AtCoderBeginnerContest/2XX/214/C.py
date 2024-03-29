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
def solve(N, S, T):
    ans = T.copy()
    for i in range(N * 2):
        x = i % N
        ans[(x + 1) % N] = min(ans[x] + S[x], ans[(x + 1) % N])
    [print(a) for a in ans]


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    S = [int(i) for i in input().split()]
    T = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(N, S, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
