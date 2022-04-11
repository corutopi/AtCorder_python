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


# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, A):
    A_num = [[A[i - 1], i] for i in range(1, N + 1)]
    Q_toK = deque(sorted(A_num[:K]))
    L_fromK = sorted(A_num[K:])
    now = -1
    ans = inf
    for x, i in L_fromK:
        while Q_toK:
            if Q_toK[0][0] >= x: break
            y, j = Q_toK.popleft()
            now = max(now, j)
        if now == -1: continue
        ans = min(ans, K - now + i - (K + 1) + 1)
    print(ans if ans != inf else -1)


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
