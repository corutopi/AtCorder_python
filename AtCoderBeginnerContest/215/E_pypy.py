# 解説を参考に作成
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
def solve(N, S):
    C_NUM = 10
    # alp to num
    alp_dict = {'ABCDEFGHIJ'[i]: i for i in range(C_NUM)}
    I = [alp_dict[s] for s in S]

    # dp[joined_map][last_joined]
    dp = [[0] * C_NUM for _ in range(2 ** C_NUM)]
    for i in I:
        new_dp = [[0] * C_NUM for _ in range(2 ** C_NUM)]
        for j, k in ((j, k) for j in range(2 ** C_NUM) for k in range(C_NUM)):
            # 出場しない場合
            new_dp[j][k] += dp[j][k]
            new_dp[j][k] %= mod2
            if i == k:
                # 前回と同じコンテスト区分で出場する場合
                new_dp[j][k] += dp[j][k]
                new_dp[j][k] %= mod2
                # 今回初めてのコンテスト区分で出場する場合
                if not j >> i & 1:
                    new_dp[j | (1 << i)][i] += sum(dp[j])
                    new_dp[j | (1 << i)][i] %= mod2
        new_dp[1 << i][i] += 1
        dp = new_dp
    print(sum([sum(x) for x in dp]) % mod2)


if __name__ == '__main__':
    N = int(input())
    S = input()
    solve(N, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 1000
    # S = random_str(1000, 'ABCDEFGHIJ')
    # print(S)
    # solve(N, S)
