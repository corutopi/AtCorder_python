# 解説などを参考に作成
"""
N = 10, LR = [2, 4] を例とする.
fi:=マスiまで移動する方法の個数とおく.
便宜上0マスから始めると、
    N:  0 1 2 3 4 5 6 7 8 9 10
    fi: 0 1 0 1 1 2 2 4 5 8 11
となる.(1マス目には最初からいるのでf1 = 1とする.)
ここで、N=5,6の時で考えると、LR=[2,4]から
    f5 = f1 + f2 + f3  (∵2～4マス前からしか遷移がないので)
    f6 =      f2 + f3 + f4
よってf5とf6の差はf1とf4によって求めることができる.
    f6 = f5 - f1 + f4
一般化すると、
    fi = fi-1 - fi-1-R + fi-L
LRが複数ある場合でも区間が重複しないので、各区間に対して - fi-1-R + fi-L 部分を計算して fi を求めることができる.
計算量はO(KN) (K:=重複しない区間LRの個数)
"""


# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, LR):
    mod = 998244353
    dp = [0] * (N + 1)
    dp[1] = 1
    # dp[0] は基本0として扱ってよいが, dp[2]の計算時のみ,dp[0]とdp[1]の差分=0となる必要がある.
    # => この時のみ、dp[0]を1として計算しないと fi = fi-1 - fi-1-R + fi-L のルールに合わなくなる.
    # 他の人の解答(#16897281, #16895566)見ると階差数列？的なのを持つことで解決できそうだったけど,
    # 内容が理解できなかったのでdp[2]までは手動実装することにした.
    dp[2] = 1 if 1 in [lr[0] for lr in LR] else 0
    for i in range(3, N + 1):
        x = 0
        for l, r in LR:
            x += dp[max(i - l, 0)] - dp[max(i - 1 - r, 0)]
        dp[i] = (dp[i - 1] + x) % mod
    print(dp[N])


if __name__ == '__main__':
    N, K = map(int, input().split())
    LR = [[int(i) for i in input().split()] for _ in range(K)]
    solve(N, K, LR)

    # # test
    # from random import randint
    # from func import random_str
    # N, K = 2 * 10 ** 5, 1
    # LR = [[1, N]]
    # solve(N, K, LR)
