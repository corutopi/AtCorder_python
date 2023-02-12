# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# import string
from heapq import heappush, heappop
from math import ceil, floor

inf = 10 ** 18
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, S):
    broken = [[inf] * W for _ in range(H)]
    dq = deque([[0, 0, 0]])
    broken[0][0] = 0
    new_dq = deque([])
    while dq:
        b, h, w = dq.popleft()
        # 上下左右の道
        if h > 0 and S[h - 1][w] == '.' and broken[h - 1][w] > b:
            broken[h - 1][w] = b
            dq.append([b, h - 1, w])
        if h < H - 1 and S[h + 1][w] == '.' and broken[h + 1][w] > b:
            broken[h + 1][w] = b
            dq.append([b, h + 1, w])
        if w > 0 and S[h][w - 1] == '.' and broken[h][w - 1] > b:
            broken[h][w - 1] = b
            dq.append([b, h, w - 1])
        if w < W - 1 and S[h][w + 1] == '.' and broken[h][w + 1] > b:
            broken[h][w + 1] = b
            dq.append([b, h, w + 1])
        # 壊して進める場所
        for hh, ww in ((i, j) for i in range(-2, 3) for j in range(-2, 3)):
            if h + hh < 0 or H <= h + hh or w + ww < 0 or W <= w + ww: continue
            if hh in [-2, 2] and ww in [-2, 2]: continue
            if S[h + hh][w + ww] == '#' and broken[h + hh][w + ww] > b + 1:
                broken[h + hh][w + ww] = b + 1
                new_dq.append([b + 1, h + hh, w + ww])
        if not dq:
            dq = new_dq
            new_dq = deque([])
    # [print(a) for a in broken]
    # print('----------------')
    print(broken[-1][-1])


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # H, W = 500, 500
    # S = [random_str(W, '#') for _ in range(H)]
    # solve(H, W, S)
