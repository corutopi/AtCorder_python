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


def get_score():
    int(input())
    return 0


def get_path(a, b, x, y):
    # int(input())
    pass


grid = [[0] * 30 for _ in range(30)]
for _ in range(1000):
    si, sj, ti, tj = map(int, input().split())
    path = ('D' if si < ti else 'U') * abs(si - ti) + \
           ('R' if sj < tj else 'L') * abs(sj - tj)
    print(path, flush=True)
    score = get_score()
