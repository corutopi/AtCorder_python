# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, A):
    inf = 2000 ** 2
    A = ['#' * (W + 2)] + ['#' + a + '#' for a in A] + ['#' * (W + 2)]
    S = []
    G = []
    warp_point = {}
    warp_used = {}
    for s in 'abcdefghijklmnopqrstuvwxyz':
        warp_point[s] = []
        warp_used[s] = False
    for h in range(H + 2):
        for w in range(W + 2):
            s = A[h][w]
            if s == 'S':
                S = [h, w]
            elif s == 'G':
                G = [h, w]
            elif not s in ['#', '.']:
                warp_point[s].append([h, w])

    dq = deque([S + [0]])
    move_map = [[inf for _ in range(W + 2)] for _ in range(H + 2)]
    move_map[S[0]][S[1]] = 0
    while dq:
        h, w, m = dq.popleft()
        s = A[h][w]
        if s not in ['S', 'G', '#', '.']:
            if not warp_used[s]:
                for hh, ww in warp_point[s]:
                    if move_map[hh][ww] > m + 1:
                        move_map[hh][ww] = m + 1
                        dq.append([hh, ww, m + 1])
                warp_used[s] = True
        for hh, ww in [[h + 1, w], [h - 1, w], [h, w + 1], [h, w - 1]]:
            if A[hh][ww] == '#':
                continue
            if move_map[hh][ww] > m + 1:
                move_map[hh][ww] = m + 1
                dq.append([hh, ww, m + 1])
    print(move_map[G[0]][G[1]] if move_map[G[0]][G[1]] < inf else -1)


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]
    solve(H, W, A)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
