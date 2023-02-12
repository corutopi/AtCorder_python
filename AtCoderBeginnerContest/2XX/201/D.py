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
def solve(H, W, A):
    score = [[0 for _ in range(W)] for _ in range(H)]

    def s(i, j):
        return 1 if A[i][j] == '+' else -1

    for h, w in reversed([(h, w) for w in range(W) for h in range(H)]):
        t = 1 if (h + w) % 2 == 0 else -1
        if h == H - 1 and w == W - 1:
            continue
        if h == H - 1:
            score[h][w] = score[h][w + 1] + s(h, w + 1) * t
            continue
        if w == W - 1:
            score[h][w] = score[h + 1][w] + s(h + 1, w) * t
            continue
        score[h][w] = max(score[h + 1][w] + s(h + 1, w) * t,
                          score[h][w + 1] + s(h, w + 1) * t) if t == 1 else \
            min(score[h + 1][w] + s(h + 1, w) * t,
                score[h][w + 1] + s(h, w + 1) * t)

    print('Draw' if score[0][0] == 0 else
          'Takahashi' if score[0][0] > 0 else
          'Aoki')


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    solve(H, W, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # H, W = 2000, 1999
    # A = [random_str(W, '+-') for _ in range(H)]
    # solve(H, W, A)
