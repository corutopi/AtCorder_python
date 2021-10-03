# 解説と以下を参考に作成
#   https://atcoder.jp/contests/abc219/submissions/26270372
"""
・実行時間が微妙なときは関数(solver)外したほうが早い
・infに使う値はなるべく実態に即して小さくした方が早い
    - float('inf') より 1000 のほうが早い
"""
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor


inf = 10000
N = int(input())
X, Y = map(int, input().split())
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
AB = [[int(i) for i in input().split()] for _ in range(N)]
# P = [int(input()) for _ in range(N)]
dp = [[[inf] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
for n in range(1, N + 1):
    a, b = AB[n - 1]
    for x, y in ((x, y) for x in range(X + 1) for y in range(Y + 1)):
        dp[n][min(x + a, X)][min(y + b, Y)] = min(
            dp[n][min(x + a, X)][min(y + b, Y)], dp[n - 1][x][y] + 1)
        dp[n][x][y] = min(dp[n][x][y], dp[n - 1][x][y])

print(dp[N][X][Y] if dp[N][X][Y] != inf else -1)