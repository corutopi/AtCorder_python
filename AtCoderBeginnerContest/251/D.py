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
def solve(W):
    ans = [i for i in range(1, 100)]
    ans += [i * 100 for i in range(1, 100)]
    ans += [i * 10000 for i in range(1, 100)]
    ans += [1000000]
    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    W = int(input())
    solve(W)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
