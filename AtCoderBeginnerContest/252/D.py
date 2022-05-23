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
def solve(N, A):
    numbers = [0] * (max(A) + 1)
    for a in A:
        numbers[a] += 1
    dp = [1] + [0] * 3
    for i in range(1, len(numbers)):
        new_dp = [1] + [0] * 3
        for j in range(1, 4):
            new_dp[j] = dp[j] + dp[j - 1] * numbers[i]
        dp = new_dp
    print(dp[-1])


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
