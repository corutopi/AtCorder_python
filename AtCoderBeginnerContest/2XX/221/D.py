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
def solve(N, AB):
    loginout = []
    for a, b in AB:
        loginout.append([a, 1])
        loginout.append([a + b, 0])
    loginout.sort()
    ans = [0] * (N + 1)
    now_menber = 0
    day = 1
    for newday, inout in loginout:
        if day < newday:
            ans[now_menber] += newday - day
            day = newday
        now_menber += 1 if inout == 1 else -1
    print(' '.join([str(i) for i in ans[1:]]))


if __name__ == '__main__':
    N = int(input())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
