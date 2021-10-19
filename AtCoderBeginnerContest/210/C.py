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
def solve(N, K, C):
    candict = {}
    for i, c in enumerate(C):
        candict.setdefault(c, i)
    canlist = [candict[c] for c in C]
    havecan = [0] * N
    candy = 0
    ans = 0
    for i in range(N):
        if havecan[canlist[i]] == 0:
            candy += 1
        havecan[canlist[i]] += 1
        if i >= K:
            havecan[canlist[i - K]] -= 1
            if havecan[canlist[i - K]] == 0:
                candy -= 1
        ans = max(ans, candy)
    print(ans)


if __name__ == '__main__':
    N, K = map(int, input().split())
    C = [int(i) for i in input().split()]
    solve(N, K, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 3 * 10 ** 5
    # K = randint(1, N)
    # C = [randint(1, 10 ** 9) for _ in range(N)]
    # solve(N, K, C)
