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

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    import string
    if len(S) != 8:
        print('No')
        return
    if S[0] not in string.ascii_uppercase:
        print('No')
        return
    if S[-1] not in string.ascii_uppercase:
        print('No')
        return
    if not S[1:-1].isnumeric():
        print('No')
        return
    if not(100000 <= int(S[1:-1]) <= 999999):
        print('No')
        return
    print('Yes')


if __name__ == '__main__':
    S = input()
    solve(S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
