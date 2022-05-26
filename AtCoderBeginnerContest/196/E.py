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
def solve(N, AT, Q, X):
    add = 0
    fx_min = - 10 ** 18
    fx_max = 10 ** 18
    for a, t in AT:
        if t == 1:
            add += a
        elif t == 2:
            fx_min = a - add if fx_min + add < a else fx_min
            fx_max = a - add if fx_max + add < a else fx_max
        else:
            fx_min = a - add if fx_min + add > a else fx_min
            fx_max = a - add if fx_max + add > a else fx_max

    for x in X:
        ans = 0
        if x < fx_min:
            ans = fx_min + add
        elif fx_min <= x <= fx_max:
            ans = x + add
        elif fx_max < x:
            ans = fx_max + add
        print(ans)


if __name__ == '__main__':
    N = int(input())
    AT = [[int(i) for i in input().split()] for _ in range(N)]
    Q = int(input())
    X = list(map(int, input().split()))
    solve(N, AT, Q, X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
