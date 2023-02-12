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
def solve(N, A, B):
    for i in range(N * A):
        s = ''
        for j in range(N * B):
            s += '.' if (i // A % 2 + j // B % 2) % 2 == 0 else '#'
        print(s)


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    solve(N, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
