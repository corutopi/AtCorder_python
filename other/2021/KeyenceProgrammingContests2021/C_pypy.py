"""
解説と以下を参考に作成
https://atcoder.jp/contests/keyence2021/submissions/19478129
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


def inverse(a, p):
    """逆元"""
    a_, p_ = a, p
    x, y = 1, 0
    while p_:
        t = a_ // p_
        a_ -= t * p_
        a_, p_ = p_, a_
        x -= t * y
        x, y = y, x
    x %= p
    return x


# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, K, hwc):
    c_i = {'R': 1, 'D': 2, 'X': 3}
    char_map = [[-1] * (W + 2)] + \
               [[-1] + [0] * W + [-1] for _ in range(H)] + \
               [[-1] * (W + 2)]
    for h, w, c in hwc:
        char_map[h][w] = c_i[c]

    # dp[h][w] すべての盤面における, (1,1) → (h, w) の経路数
    dp = [[0] * (W + 2) for _ in range(H + 2)]
    dp[1][1] = pow(3, H * W - K, mod2)  # スタート位置は盤面の数
    inv3 = inverse(3, mod2)
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if h == w == 1:
                continue
            # from left
            if char_map[h][w - 1] == 0:  # 空白の場合
                dp[h][w] += ((dp[h][w - 1] * 2) * inv3) % mod2
            elif char_map[h][w - 1] == 1 or char_map[h][w - 1] == 3:
                dp[h][w] += dp[h][w - 1]
            # from up
            if char_map[h - 1][w] == 0:  # 空白の場合
                dp[h][w] += ((dp[h-1][w] * 2) * inv3) % mod2
            elif char_map[h - 1][w] == 2 or char_map[h - 1][w] == 3:
                dp[h][w] += dp[h - 1][w]

            dp[h][w] %= mod2

    print(dp[H][W])


if __name__ == '__main__':
    H, W, K = map(int, input().split())
    hwc = [[int(s) if i < 2 else s for i, s in enumerate(input().split())] for _
           in range(K)]
    solve(H, W, K, hwc)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve(5000, 5000, 0, [])
