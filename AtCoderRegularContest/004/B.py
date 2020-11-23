# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
import numpy as np
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, d):
    ans_max = sum(d)
    ans_min = ans_max
    d = np.array([0] + d)
    d_cs = d.cumsum()
    l, r = 0, 1
    while r != N + 1:
        a = d_cs[l]
        b = d_cs[r] - d_cs[l]
        c = ans_max - a - b
        ans_min = min(ans_min, max(0, max(a, b, c) * 2 - sum([a, b, c])))
        if ans_min == 0:
            break
        if b > ans_max / 2:
            l += 1
        else:
            r += 1
    print(ans_max)
    print(ans_min)


if __name__ == '__main__':
    N = int(input())
    d = [int(input()) for _ in range(N)]
    solve(N, d)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
