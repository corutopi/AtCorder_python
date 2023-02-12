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
def solve(H, W, N, AB):
    mass_dict = {}
    for a, b in AB:
        for aa, bb in ((aa, bb)
                       for aa in range(max(1, a - 2), min(a, H - 2) + 1)
                       for bb in range(max(1, b - 2), min(b, W - 2) + 1)):
            tmp = aa * W + bb
            mass_dict.setdefault(tmp, 0)
            mass_dict[tmp] += 1
    ans = [0] * 10
    ans[0] = (H - 2) * (W - 2)
    for k, v in mass_dict.items():
        ans[0] -= 1
        ans[v] += 1
    [print(a) for a in ans]


if __name__ == '__main__':
    H, W, N = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(H, W, N, AB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
