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
def solve(N, M, K, S, T, X, UV):
    S -= 1
    T -= 1
    X -= 1
    graph_map = [[] for _ in range(N)]
    for u, v in UV:
        graph_map[u - 1].append(v - 1)
        graph_map[v - 1].append(u - 1)
    dp = [[0, 0] for _ in range(N)]
    dp[S][0] = 1
    for _ in range(K):
        new_dp = [[0, 0] for _ in range(N + 1)]
        for i in range(N):
            for g in graph_map[i]:
                if g == X:
                    new_dp[g][1] += dp[i][0]
                    new_dp[g][0] += dp[i][1]
                else:
                    new_dp[g][0] += dp[i][0]
                    new_dp[g][1] += dp[i][1]
                new_dp[g][0] %= mod2
                new_dp[g][1] %= mod2
        dp = new_dp
    print(dp[T][0])


if __name__ == '__main__':
    N, M, K, S, T, X = map(int, input().split())
    UV = [[int(i) for i in input().split()] for _ in range(M)]
    solve(N, M, K, S, T, X, UV)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
