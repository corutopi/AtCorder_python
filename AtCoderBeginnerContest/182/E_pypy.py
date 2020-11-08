# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, N, M, AB, CD):
    # kind, islight, search top, bottom, left, right
    hw_map = [[[1, 0, 0, 0, 0, 0] for _ in range(W + 2)]] + \
             [[[1, 0, 0, 0, 0, 0]] + [[0, 0, 0, 0, 0, 0] for _ in range(W)] + [
                 [1, 0, 0, 0, 0, 0]] for _ in range(H)] + \
             [[[1, 0, 0, 0, 0, 0] for _ in range(W + 2)]]
    for a, b in AB:
        hw_map[a][b][0] = 2
    for c, d in CD:
        hw_map[c][d][0] = 1
    ans = 0
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            k, isl, t, b, l, r = hw_map[h][w]
            if k != 2:
                continue
            # 自分自身
            ans += 1
            hw_map[h][w][2] = 1
            if t == 0:
                ht = h - 1
                while hw_map[ht][w][0] == 0:
                    if hw_map[ht][w][2] == 0:
                        ans += 1
                        hw_map[ht][w][2] += 1
                    ht -= 1
            if b == 0:
                hb = h + 1
                while hw_map[hb][w][0] == 0:
                    if hw_map[hb][w][2] == 0:
                        ans += 1
                        hw_map[hb][w][2] += 1
                    hb += 1
                if hw_map[hb][w][0] == 2:
                    hw_map[hb][w][2] = 1
            if l == 0:
                wl = w - 1
                while hw_map[h][wl][0] == 0:
                    if hw_map[h][wl][2] == 0:
                        ans += 1
                        hw_map[h][wl][2] += 1
                    wl -= 1
            if r == 0:
                wr = w + 1
                while hw_map[h][wr][0] == 0:
                    if hw_map[h][wr][2] == 0:
                        ans += 1
                        hw_map[h][wr][2] += 1
                    wr += 1
                if hw_map[h][wr][2] == 2:
                    hw_map[h][wr][4] = 1
    print(ans)


if __name__ == '__main__':
    H, W, N, M = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    CD = [[int(i) for i in input().split()] for _ in range(M)]
    solve(H, W, N, M, AB, CD)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # H, W, N, M = 1500, 1500, 1, 1
    # AB = [[i, i] for i in range(1, H + 1)]
    # CD = [[1,6]]
    #
    # solve(H, W, N, M, AB, CD)
