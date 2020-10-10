# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, S):
    mod = 10 ** 9 + 7
    S = ['#' * (W + 2)] + ['#' + s + '#' for s in S] + ['#' * (W + 2)]
    lamp_num = 0
    lamp_map = [[[0, 0] for _ in range(W + 2)] for _ in range(H + 2)]

    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if S[h][w] == '#':
                continue
            lamp_num += 1
            if lamp_map[h - 1][w][0] != 0:
                lamp_map[h][w][0] = lamp_map[h - 1][w][0]
            else:
                tmp_h = 0
                while S[h + tmp_h][w] == '.':
                    tmp_h += 1
                lamp_map[h][w][0] = tmp_h

            if lamp_map[h][w - 1][1] != 0:
                lamp_map[h][w][1] = lamp_map[h][w - 1][1]
            else:
                tmp_w = 0
                while S[h][w + tmp_w] == '.':
                    tmp_w += 1
                lamp_map[h][w][1] = tmp_w

    exp2_map = [1]
    for _ in range(lamp_num):
        exp2_map.append((exp2_map[-1] * 2) % mod)

    ans = 0
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if S[h][w] == '#':
                continue
            light_lamp = sum(lamp_map[h][w]) - 1
            ans += exp2_map[lamp_num - light_lamp] * (exp2_map[light_lamp] - 1)
            ans %= mod

    print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    solve(H, W, S)

    # # test
    # from random import randint
    # from func import random_str
    # H, W = 2, 2
    # S = [random_str(W, '.') for _ in range(H)]
    # solve(H, W, S)
    # H, W = 3, 3
    # S = ['###', '#.#', '###']
    # solve(H, W, S)
