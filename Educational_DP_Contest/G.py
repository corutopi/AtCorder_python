"""
G - Longest Path

考え方:
    頂点 n までの最大パスを, y = n である有向パスのすべての x の最大パス n' + 1 の中で最大のものから求める.
    x の最大パスが計算されていない場合は先に x の最大パスを同じ方法で求める.
    y = n となる有効パスが存在しない場合, n の最大パスは 0 とする. 有効閉路は存在しないのでループは発生しない.
    計算量は O(N + M) = O(2n) = O(n) .

提出1回目の反省:
    debug 用の print 外し忘れてた

提出2回目の反省:
    なぜ RE になるんじゃぁ
    -> python の最大再帰回数の問題である可能性. あんまりよくない気もするけど設定変更してみよう.

提出3回目の反省:
    10000 に設定してみたけどケース1_01ではじかれる. どうも設定値 - 1回目の呼び出しでエラーになるようだ.
    少し余裕をもって10020と設定.

提出4回目の反省:
    それでもケース1_01がダメ. なぜ...

完了後反省:
    やっぱ閾値狙ったりせずに余裕持って設定したほうがええな.
"""

import sys

sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().split())
Y = [[] for _ in range(N + 1)]
# print(len(Y), Y)
for _ in range(M):
    x, y = map(int, input().split())
    Y[y].append(x)

dp = [-1] * (N + 1)


def solve(num):
    re = 0
    if dp[num] != -1:
        # すでに計算済みのパスは再計算しない.
        re = dp[num]
    else:
        for x in Y[num]:
            if dp[x] == -1:
                dp[x] = solve(x)
            re = max(re, dp[x] + 1)
    return re


for n in range(1, N + 1):
    dp[n] = solve(n)

print(max(dp))
