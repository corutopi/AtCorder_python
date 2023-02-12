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
def solve(V, A, B, C):
    fam = A + B + C
    V -= V // fam * fam
    if V < A:
        print('F')
    elif V < A + B:
        print('M')
    else:
        print('T')


if __name__ == '__main__':
    V, A, B, C = map(int, input().split())
    solve(V, A, B, C)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
