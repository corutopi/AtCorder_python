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
def solve(H, W, N, RCA):
    XRCA = [[i] + RCA[i] for i in range(N)]
    XRCA.sort(reverse=True, key=lambda x: x[3])

    h_max = [0] * H
    w_max = [0] * W
    ans = [0] * N

    now = inf
    h_stack = []
    w_stack = []
    for i in range(N):
        x, r, c, a = XRCA[i]
        r -= 1
        c -= 1
        if now != a:
            while h_stack:
                rr, num = h_stack.pop()
                h_max[rr] = max(h_max[rr], num)
            while w_stack:
                cc, num = w_stack.pop()
                w_max[cc] = max(w_max[cc], num)
        now = a
        ans[x] = max(h_max[r], w_max[c])
        h_stack.append([r, ans[x] + 1])
        w_stack.append([c, ans[x] + 1])
    [print(a) for a in ans]




if __name__ == '__main__':
    H, W, N = map(int, input().split())
    RCA = [[int(i) for i in input().split()] for _ in range(N)]
    solve(H, W, N, RCA)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
