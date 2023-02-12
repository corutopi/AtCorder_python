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
def solve(N, K, A, B):
    dp = [A[0], B[0]]
    for i in range(N):
        new_dp = [0, 0]
        for j in range(2):
            if dp[j] == 0: continue
            # select A
            if abs(dp[j] - A[i]) <= K:
                new_dp[0] = A[i]
            # select B
            if abs(dp[j] - B[i]) <= K:
                new_dp[1] = B[i]

        # update dp
        dp = new_dp
    print('Yes' if sum(dp) > 0 else 'No')


if __name__ == '__main__':
    N, K = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(N, K, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
