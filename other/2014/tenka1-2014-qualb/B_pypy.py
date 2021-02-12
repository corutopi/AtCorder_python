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
def solve(N, S, T):
    dp = [[0] * N for _ in range(len(S) + 1)]  #[i文字目][i文字目にTjを使用するパターン数]

    # initialize
    for t in range(N):
        if T[t] == S[:len(T[t])]:
            dp[1][t] = 1

    # dp
    for i in range(2, len(S) + 1):
        for j in range(N):
            if T[j] != S[i - 1:i - 1 + len(T[j])]: continue
            for k in range(N):
                dp[i][j] += dp[max(0, i - len(T[k]))][k]
            dp[i][j] %= mod
    ans = sum([dp[len(S) + 1 - len(T[j])][j] for j in range(N)])
    ans %= mod
    print(ans)



if __name__ == '__main__':
    N = int(input())
    S = input()
    T = [input() for _ in range(N)]
    solve(N, S, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 100
    # S = 'a' * 1000
    # T = ['a' * i for i in range(1, N + 1)]
    # solve(N, S, T)
