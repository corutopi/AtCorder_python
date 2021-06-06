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
def solve(H, W, A):
    c_sum = [0] * W
    r_sum = [0] * H
    for w in range(W):
        tmp = 0
        for h in range(H):
            tmp += A[h][w]
        c_sum[w] = tmp
    for h in range(H):
        r_sum[h] = sum(A[h])
    B = [[0] * W for _ in range(H)]
    for h, w in ((h, w) for h in range(H) for w in range(W)):
        B[h][w] = str(r_sum[h] + c_sum[w] - A[h][w])
    [print(' '.join(b)) for b in B]


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]
    solve(H, W, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # H, W = 2000, 2000
    # A = [[randint(1, 99) for _ in range(W)] for _ in range(H)]
    # solve(H, W, A)
