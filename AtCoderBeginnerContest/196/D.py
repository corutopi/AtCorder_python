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
def solve(H, W, A, B):
    room = [[0] * W for _ in range(H)]
    ans = 0
    tile = [0, 0]
    a, b = 0, 1

    def dfs(r):
        if r == H * W:
            return 1
        h, w = divmod(r, W)
        # 既にタイルが埋められている場合
        if room[h][w] == 1:
            return dfs(r + 1)
        # タイルをはめる場合
        re = 0
        # # 正方形のタイルを使う
        if tile[b] + 1 <= B:
            tile[b] += 1
            room[h][w] = 1
            re += dfs(r + 1)
            room[h][w] = 0
            tile[b] -= 1
        # # 長方形のタイルを使う(横)
        if tile[a] + 1 <= A and w + 1 < W and room[h][w + 1] == 0:
            tile[a] += 1
            room[h][w], room[h][w + 1] = 1, 1
            re += dfs(r + 2)
            room[h][w], room[h][w + 1] = 0, 0
            tile[a] -= 1
        # # 長方形のタイルを使う(縦)
        if tile[a] + 1 <= A and h + 1 < H and room[h + 1][w] == 0:
            tile[a] += 1
            room[h][w], room[h + 1][w] = 1, 1
            re += dfs(r + 1)
            room[h][w], room[h + 1][w] = 0, 0
            tile[a] -= 1
        return re

    print(dfs(0))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    H, W, A, B = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(H, W, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
