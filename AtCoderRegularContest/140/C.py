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
def solve(N, X):
    ans = [X]
    p = 0
    if N % 2 == 1:
        now = N // 2 + 1
        v = -1 if X < now else 1
    else:
        if N // 2 < X:
            now = N // 2
            v = 1 if now == X else -1
        else:
            now = N // 2 + 1
            v = -1 if now == X else 1
    for i in range(N - 1):
        if now == X:
            now += v
            p += 1
        ans.append(now)
        v *= -1
        p += 1
        now += p * v
    print(*ans)


if __name__ == '__main__':
    N, X = map(int, input().split())
    solve(N, X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
