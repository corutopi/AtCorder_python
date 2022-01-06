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
def solve(N, a):
    ma = 0
    for i in range(1, N):
        ma = i if abs(a[i]) > abs(a[ma]) else ma

    ans = []
    if a[ma] >= 0:
        for i in range(N):
            if a[i] < 0:
                ans.append([ma, i])
                a[i] += a[ma]
        for i in range(N - 1):
            a[i + 1] += a[i]
            ans.append([i, i + 1])
    else:
        for i in range(N):
            if a[i] >= 0:
                ans.append([ma, i])
                a[i] += a[ma]
        for i in range(N - 1, 0, -1):
            a[i - 1] += a[i]
            ans.append([i, i - 1])
    # print(a)
    print(len(ans))
    [print(*[aa + 1 for aa in a]) for a in ans]


if __name__ == '__main__':
    N = int(input())
    a = [int(i) for i in input().split()]
    solve(N, a)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
