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
def solve(N, Q, X):
    ball = [i for i in range(N + 1)]
    posi = [i for i in range(N + 1)]
    for x in X:
        now = posi[x]
        now = now - 1 if now == N else now
        a, b = ball[now], ball[now + 1]
        ball[now], ball[now + 1] = b, a
        posi[a], posi[b] = now + 1, now
    print(*ball[1:])


if __name__ == '__main__':
    N, Q = map(int, input().split())
    X = [int(input()) for _ in range(Q)]
    solve(N, Q, X)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
