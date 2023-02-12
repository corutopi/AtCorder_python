# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, S):
    S = ['#' * (W + 2)] + ['#' + s + '#' for s in S] + ['#' * (W + 2)]
    p_map = [[0] * (W + 2) for _ in range(H + 2)]
    p_sum_map_r = [[0] * (W + 2) for _ in range(H + 2)]
    p_sum_map_d = [[0] * (W + 2) for _ in range(H + 2)]
    p_sum_map_rd = [[0] * (W + 2) for _ in range(H + 2)]
    p_map[1][1] = 1
    p_sum_map_r[1][1] = 1
    p_sum_map_d[1][1] = 1
    p_sum_map_rd[1][1] = 1
    mod = 10 ** 9 + 7
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if h == 1 and w == 1:
                continue
            if S[h][w] == '#':
                continue
            p_map[h][w] = (p_sum_map_r[h][w - 1] +
                           p_sum_map_d[h - 1][w] +
                           p_sum_map_rd[h - 1][w - 1]) % mod
            p_sum_map_r[h][w] = p_map[h][w] + p_sum_map_r[h][w - 1]
            p_sum_map_d[h][w] = p_map[h][w] + p_sum_map_d[h - 1][w]
            p_sum_map_rd[h][w] = p_map[h][w] + p_sum_map_rd[h - 1][w - 1]

    print(p_map[H][W])


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    #
    # H = W = 2000
    # S = ['.' * W for _ in range(H)]
    # solve(H, W, S)
