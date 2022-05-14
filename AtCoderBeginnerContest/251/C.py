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
def solve(N, ST):
    poem_dict = dict()
    max_point = 0
    ans = 1
    for i in range(N):
        s, t = ST[i]
        t = int(t)
        if poem_dict.get(s, -1) == -1:
            poem_dict[s] = t
            if max_point < t:
                max_point = t
                ans = i + 1
    print(ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    ST = [input().split() for _ in range(N)]
    solve(N, ST)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
