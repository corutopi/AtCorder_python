# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
# mod = 10 ** 9 + 7
mod = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A, B):
    border = max(A) + 1
    AB = [[a, b] for a, b in zip(A, B)]
    AB.sort()

    dp = [0] * border
    dp[0] = 1
    ans = 0
    for a, b in AB:
        for n in reversed(range(b, border)):
            if dp[n - b] > 0:
                ans += dp[n - b] if n <= a else 0
                dp[n] += dp[n - b]
                dp[n] %= mod
        ans %= mod
    print(ans)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(N, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # while True:
    #     N = 500
    #     A = random_ints(N, 4000, 5000)
    #     B = random_ints(N, 4000, 5000)
    #     solve(N, A, B)
