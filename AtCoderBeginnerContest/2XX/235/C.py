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
def solve(N, Q, a, xk):
    dict = {}
    for i in range(N):
        dict.setdefault(a[i], [])
        dict[a[i]].append(i + 1)
    for x, k in xk:
        if dict.get(x, -1) == -1:
            print(-1)
            continue
        tmp = dict[x]
        if len(tmp) < k:
            print(-1)
            continue
        print(tmp[k - 1])


if __name__ == '__main__':
    N, Q = map(int, input().split())
    a = [int(i) for i in input().split()]
    xk = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, a, xk)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 2 * 10 ** 5
    # Q = 2 * 10 ** 5
    # a = random_ints(N, 0, 20)
    # xk = [[randint(0, 20), randint(1, 100)] for _ in range(Q)]
    # solve(N, Q, a, xk)
