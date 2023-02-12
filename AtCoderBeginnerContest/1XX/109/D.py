# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, A):
    move = []
    for h in range(H):
        for w in range(W):
            if A[h][w] % 2 == 1:
                if h < H - 1 and A[h + 1][w] % 2 == 1:
                    A[h][w] -= 1
                    A[h + 1][w] += 1
                    move.append([h, w, h + 1, w])
                elif w < W - 1 and A[h][w + 1] % 2 == 1:
                    A[h][w] -= 1
                    A[h][w + 1] += 1
                    move.append([h, w, h, w + 1])
                elif h < H - 1:
                    A[h][w] -= 1
                    A[h + 1][w] += 1
                    move.append([h, w, h + 1, w])
                elif w < W - 1:
                    A[h][w] -= 1
                    A[h][w + 1] += 1
                    move.append([h, w, h, w + 1])
    print(len(move))
    for m in move:
        print(' '.join([str(i + 1) for i in m]))


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]
    solve(H, W, A)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
