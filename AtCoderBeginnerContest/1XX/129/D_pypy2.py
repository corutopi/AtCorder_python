# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, Si):
    R = [[0] * W for _ in range(H)]
    L = [[0] * W for _ in range(H)]
    D = [[0] * W for _ in range(H)]
    U = [[0] * W for _ in range(H)]

    # for R
    for h in range(H):
        for w in range(W):
            if Si[h][w] == '#':
                R[h][w] = 0
                continue
            if w == 0:
                R[h][w] = 1
            else:
                R[h][w] = R[h][w - 1] + 1
    # for L
    for h in range(H):
        for w in range(W):
            if Si[h][W - w - 1] == '#':
                L[h][W - w - 1] = 0
                continue
            if w == 0:
                L[h][W - w - 1] = 1
            else:
                L[h][W - w - 1] = L[h][W - w] + 1
    # for D
    for w in range(W):
        for h in range(H):
            if Si[h][w] == '#':
                D[h][w] = 0
                continue
            if h == 0:
                D[h][w] = 1
            else:
                D[h][w] = D[h - 1][w] + 1
    # for U
    for w in range(W):
        for h in range(H):
            if Si[H - h - 1][w] == '#':
                U[H - h - 1][w] = 0
                continue
            if h == 0:
                U[H - h - 1][w] = 1
            else:
                U[H - h - 1][w] = U[H - h][w] + 1

    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, R[h][w] + L[h][w] + D[h][w] + U[h][w] - 3)
    print(ans)


if __name__ == '__main__':
    H, W = map(int, input().split())
    Si = [input() for _ in range(H)]

    # # test
    # import func
    # H, W = 2000, 2000
    # Si = [''.join([func.random_str(W, '.')]) for _ in range(H)]
    # for s in Si:
    #     print(s)
    solve(H, W, Si)
