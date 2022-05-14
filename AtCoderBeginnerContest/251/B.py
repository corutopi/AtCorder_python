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
def solve(N, W, A):
    ans = [0] * (W + 1)
    A = [0] + A
    for i in range(N + 1):
        for j in range(i, N + 1):
            if i == j and i != 0:
                continue
            for k in range(j, N + 1):
                if (i == k or j == k) and k != 0:
                    continue
                if 0 < A[i] + A[j] + A[k] <= W:
                    ans[A[i] + A[j] + A[k]] = 1
    print(sum(ans))


if __name__ == '__main__':
    N, W = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(N, W, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
