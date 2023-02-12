# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(S):
    mod = 10 ** 9 + 7
    dp = [0] * (S + 1)
    dp[0] = 1
    for i in range(3, S + 1):
        dp[i] = dp[i - 1] + dp[i - 3]
        dp[i] %= mod
    print(dp[S])


if __name__ == '__main__':
    S = int(input())
    solve(S)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
