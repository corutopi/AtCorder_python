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
def solve(N, M, K):
    x = (min(N * (M - 1), K - N) + 1)
    dp = [0] * x
    dp[-1] = 1
    for i in range(N):
        # 累積和
        cumsum = [0]
        for d in dp:
            cumsum.append(cumsum[-1] + d)
        dp_new = [0] * x
        for j in range(x):
            dp_new[j] = cumsum[min(j + M, x)] - cumsum[j]
            dp_new[j] %= mod2
        dp = dp_new
    print(sum(dp) % mod2)


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    solve(N, M, K)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
