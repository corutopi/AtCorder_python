# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
from collections import deque
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
def solve(N, Q, event):
    next_call = 1
    visited = [0] * (N + 1)
    called = deque([])
    for e in event:
        if e[0] == 1:
            called.append(next_call)
            next_call += 1
        elif e[0] == 2:
            visited[e[1]] = 1
        elif e[0] == 3:
            while visited[called[0]] == 1:
                called.popleft()
            print(called[0])


if __name__ == '__main__':
    N, Q = map(int, input().split())
    event = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, Q, event)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
