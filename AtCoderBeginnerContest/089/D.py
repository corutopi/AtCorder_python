# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
inf = float('inf')
mod = 10 ** 9 + 7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(H, W, D, A, Q, LR):
    A = [[]] + [[0] + a for a in A]

    num_map = [[] for _ in range(H * W + 1)]
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            num_map[A[h][w]] = [h, w]

    mod_map = [[0] for _ in range(D)]
    for d in range(1, D + 1):
        start = d
        i, j = num_map[d]
        for dd in range(start + D, H * W + 1, D):
            x, y = num_map[dd]
            mod_map[d % D].append(mod_map[d % D][-1] + abs(x - i) + abs(y - j))
            i, j = x, y

    for l, r in LR:
        tmp_mod = l % D
        if tmp_mod == 0:
            l -= D
            r -= D
        print(mod_map[tmp_mod][r // D] - mod_map[tmp_mod][l // D])


if __name__ == '__main__':
    H, W, D = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]
    Q = int(input())
    LR = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(H, W, D, A, Q, LR)

    # # test
    # from random import randint
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
