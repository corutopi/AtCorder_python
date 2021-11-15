# import sys
# sys.setrecursionlimit(10 ** 6)
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
def solve(N, A, B):
    dp = [0] * 3001
    for i in range(A[0], 3001):
        if i <= B[0]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1]

    for a, b in zip(A[1:], B[1:]):
        new_dp = [0] * 3001
        for i in range(a, 3001):
            if dp[i] == 0:
                continue
            elif i <= b:
                new_dp[i] = (new_dp[i - 1] + dp[i]) % mod2
            else:
                new_dp[i] = new_dp[i - 1]
        dp = new_dp
    print(dp[-1] % mod2)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(N, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 3000
    # A = [randint(1, 3000) for _ in range(N)]
    # B = [randint(1, 3000) for _ in range(N)]
    # solve(N, A, B)
