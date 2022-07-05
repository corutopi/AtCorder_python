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
def solve(N, X, AB):
    cumsum = [0]
    for a, b in AB:
        cumsum.append(cumsum[-1] + a + b)
    ans = inf
    for i in range(min(N, X)):
        ans = min(ans, cumsum[i + 1] + (X - i - 1) * AB[i][1])
    print(ans)


if __name__ == '__main__':
    N, X = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, X, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
