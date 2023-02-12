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
    for w in range(W):
        print(*[A[h][w] for h in range(H)])


if __name__ == '__main__':
    H, W = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(H)]
    solve(H, W, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # H, W = 173, 173
    # A = [random_ints(W, 1, 10 ** 9) for _ in range(H)]
    # solve(H,W,A)
