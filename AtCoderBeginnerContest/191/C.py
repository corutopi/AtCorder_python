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
def solve(H, W, S):
    # find start
    start = (0, 0)
    for hh, ww in ((hh, ww) for hh in range(H) for ww in range(W)):
        if S[hh][ww] == '#':
            start = (hh, ww - 1)
            break

    # work around
    up, down, left, right = 0, 1, 2, 3
    # 方向の決定
    hh, ww = start
    vector = None
    if S[hh + 1][ww] == '#':
        vector = right
    elif S[hh][ww - 1] == '#':
        vector = down
    elif S[hh - 1][ww] == '#':
        vector = left
    else:
        vector = up

    # 周回開始
    fold_cnt = 0
    first_vector = vector
    h, w = start
    while True:
        # 折るか進むかさせる
        if vector == right:
            if S[h][w + 1] == '.' and S[h + 1][w + 1] == '.':
                w += 1
                vector = down
                fold_cnt += 1
            elif S[h][w + 1] == '#':
                vector = up
                fold_cnt += 1
            else:
                w += 1

        if vector == down:
            if S[h + 1][w] == '.' and S[h + 1][w - 1] == '.':
                h += 1
                vector = left
                fold_cnt += 1
            elif S[h + 1][w] == '#':
                vector = right
                fold_cnt += 1
            else:
                h += 1

        if vector == left:
            if S[h][w - 1] == '.' and S[h - 1][w - 1] == '.':
                w -= 1
                vector = up
                fold_cnt += 1
            elif S[h][w - 1] == '#':
                vector = down
                fold_cnt += 1
            else:
                w -= 1

        if vector == up:
            if S[h - 1][w] == '.' and S[h - 1][w + 1] == '.':
                h -= 1
                vector = right
                fold_cnt += 1
            elif S[h - 1][w] == '#':
                vector = left
                fold_cnt += 1
            else:
                h -= 1

        if h == start[0] and w == start[1] and first_vector == vector:
            break

    print(fold_cnt)


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
