# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
from math import log

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def base_number(n, base):
    if n == 0:
        re = '0'
    else:
        re = ''
        a = n
        while a // base > 0:
            a, b = divmod(a, base)
            re = str(b) + re
        re = str(a) + re
    return re


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, L):
    S0 = ['0' for _ in range(N)]
    S1 = ['1' for _ in range(N)]
    S2 = ['2' for _ in range(N)]
    for _ in range(L - ceil(log(N, 3)) - 1):
        for i in range(N):
            S0[i] += '1'
            S1[i] += '2'
            S2[i] += '0'
    zan = ceil(log(N, 3))
    to0 = ''.maketrans('012', '120')
    to1 = ''.maketrans('012', '201')
    for i in range(N):
        s = ('0' * L + base_number(i, 3))
        s = s[len(s) - zan:]
        S0[i] += s.translate(to0)
        S1[i] += s.translate(to1)
        S2[i] += s
    [print(s) for s in S0]
    [print(s) for s in S1]
    [print(s) for s in S2]


if __name__ == '__main__':
    N, L = map(int, input().split())
    solve(N, L)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
    # for i in range(10):
    #     print(base_number(i, 3))
    # solve(5 * 10 ** 4, 15)
