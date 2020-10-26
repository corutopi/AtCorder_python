# 解説を参考に作成
# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, Q, LR, pq):
    train_map = [[0] * (N + 1) for _ in range(N + 1)]
    for l, r in LR:
        train_map[l][r] += 1

    train_cs = [[0] for _ in range(N + 1)]
    for i in range(len(train_map)):
        for n in train_map[i][1:]:
            train_cs[i].append(train_cs[i][-1] + n)

    for p, q in pq:
        ans = 0
        for ii in range(p, q + 1):
            ans += train_cs[ii][q] - train_cs[ii][p - 1]
        print(ans)


if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    LR = [[int(i) for i in input().split()] for _ in range(M)]
    pq = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(N, M, Q, LR, pq)

    # # test
    # from random import randint
    # from func import random_str
    #
    # N, M, Q = 500, 200000, 100000
    # LR = [sorted([randint(1, N), randint(1, N)]) for _ in range(M)]
    # pq = [[1, N] for _ in range(Q)]
    # solve(N, M, Q, LR, pq)
