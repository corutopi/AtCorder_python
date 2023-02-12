# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor

inf = 1 << 60
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, ABC):
    dp = [[inf] * N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
    for a, b, c in ABC:
        dp[a - 1][b - 1] = c
    ans = 0
    for k in range(N):
        new_dp = [[inf] * N for _ in range(N)]
        for i, j in ((i, j) for i in range(N) for j in range(N)):
            new_dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
            if new_dp[i][j] < inf:
                ans += new_dp[i][j]
        dp = new_dp
    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    ABC = [[int(i) for i in input().split()] for _ in range(M)]
    # P = [int(input()) for _ in range(N)]
    solve(N, M, ABC)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
