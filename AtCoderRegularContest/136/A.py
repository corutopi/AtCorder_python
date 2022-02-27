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
def solve(N, S):
    tmp1 = ''.join([s if s != 'A' else 'BB' for s in S])
    ans = ''
    i = 0
    while i < len(tmp1):
        if i < len(tmp1) - 1:
            if tmp1[i] == tmp1[i + 1] == 'B':
                ans += 'A'
                i += 1
            else:
                ans += tmp1[i]
        else:
            ans += tmp1[i]
        i += 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    S = input()
    solve(N, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 2 * 10 ** 5
    # S = random_str(N, 'ABC')
    # print(S)
    # solve(N, S)
