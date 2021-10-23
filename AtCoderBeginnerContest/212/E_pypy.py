"""
解説と以下を参考に作成
    https://atcoder.jp/contests/abc212/submissions/26747946
- 方針はあっていたが、計算量を削減しきれずTLE
- dp中にmap内の使用できない道の合計を算出するために内包表記でsumしてた部分がネックだった模様
    dp[h][i] = (p_sum - dp[h - 1][i] - sum((dp[h - 1][j] for j in unuse_map[i]))) % mod2
- 外に出して個別計算するようにしたら通るようになった
- 内包表記の場合でも1回のdp内で最大M*2=10**4回の計算量にしかならんと思っていたが、だめらしい
    - 実質0でもsum演算する必要があること自体が良くないのかも
"""

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

N, M, K = map(int, input().split())
UV = [[int(i) - 1 for i in input().split()] for _ in range(M)]
# unuse_map = [[] for _ in range(N)]
# for _ in range(M):
#     u, v = map(lambda x: int(x) - 1, input().split())
#     unuse_map[u].append(v)
#     unuse_map[v].append(u)
dp = [0] * N
dp[0] = 1
p_sum = 1
for _ in range(K):
    new_dp = [0] * N
    new_p_sum = 0
    for i in range(N):
        new_dp[i] += p_sum - dp[i]
        new_p_sum += new_dp[i]
    for u, v in UV:
        new_dp[u] -= dp[v]
        new_dp[v] -= dp[u]
        new_p_sum -= dp[u] + dp[v]
    dp = [n % mod2 for n in new_dp]
    p_sum = new_p_sum % mod2
print(dp[0] % mod2)

# dp = [[0] * N for _ in range(K + 1)]
# dp[0][0] = 1
# p_sum = 1
# for h in range(1, K + 1):
#     # new_dp = [0] * N
#     new_p_sum = 0
#     for i in range(N):
#         dp[h][i] = (p_sum - dp[h - 1][i] - sum((dp[h - 1][j] for j in unuse_map[i]))) % mod2
#         new_p_sum += dp[h][i]
#     p_sum = new_p_sum % mod2
# print(dp[K][0])

# # test
# from random import randint
# import string
# import tool.testcase as tt
# from tool.testcase import random_str, random_ints
# N = 5000
# M = 0
# K = 5000
# UV = []
# solve(N, M, K, UV)
