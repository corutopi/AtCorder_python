# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, A, B):
    dp = [[-1] * (M + 1) for _ in range(N + 1)]
    for n in range(N + 1):
        for m in range(M + 1):
            if n == 0:
                dp[n][m] = m
                continue
            if m == 0:
                dp[n][m] = n
                continue
            tmp = 0 if A[n - 1] == B[m - 1] else 1
            dp[n][m] = min(dp[n - 1][m] + 1,
                           dp[n][m - 1] + 1,
                           dp[n - 1][m - 1] + tmp)
    print(dp[N][M])


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    solve(N, M, A, B)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
