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
def solve(N):
    length = [[0, 0] for _ in range(N + 1)]
    ans = inf
    for i in range(3, N + 1):
        print('?', 1, i, flush=True)
        x = int(input())
        print('?', 2, i, flush=True)
        y = int(input())
        ans = min(ans, x + y)
        length[i] = [x, y]
    for a, b in length[3:]:
        if abs(a - b) != 1:
            break
    else:
        if N == 4:
            print('?', 3, 4, flush=True)
            z = int(input())
            if z == 1 and max((max(l) for l in length)) < 3:
                ans = 3
            else:
                ans = 1
        else:
            ans = 1
    print('!', ans, flush=True)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
