# 開設を参考に作成
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
def solve(N, T):
    T = [0] + T
    dp = [[False] * (sum(T) // 2 + 1) for _ in range(N + 1)]
    dp[0][0] = True
    re_ans = 0
    for i in range(1, N + 1):
        for j in range(0, (sum(T) // 2 + 1)):
            if j < T[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - T[i]]
            re_ans = max(re_ans, j) if dp[i][j] else re_ans
    print(sum(T) - re_ans)


            # def solve2(N, T):
#     ans = inf
#     for i in range(2 ** N):
#         oben_a, oben_b = 0, 0
#         for j in range(N):
#             if i >> j & 1:
#                 oben_a += T[j]
#             else:
#                 oben_b += T[j]
#         ans = min(ans, max(oben_a, oben_b))
#     return ans


if __name__ == '__main__':
    N = int(input())
    T = [int(i) for i in input().split()]
    solve(N, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 100
    # T = [1000] * N
    # solve(N, T)
    # while True:
    #     N = 5
    #     T = [randint(1, 10) for _ in range(N)]
    #     if solve(N, T) != solve2(N, T):
    #         print(T, solve(N, T), solve2(N, T))
    #         break
