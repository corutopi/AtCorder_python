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
def solve(N):
    dp = [0, 1]
    for i in range(13):
        dp.append(dp[-1] * 10 + 10 ** (i + 1))

    ans = 0
    n = N
    j = 0
    while n > 0:
        n, k = divmod(n, 10)
        if k != 0:
            ans += dp[j] * k + (N % (10 ** j) + 1 if k == 1 else 10 ** j)
        j += 1
    print(ans)


if __name__ == '__main__':
    N = int(input())
    solve(N)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
