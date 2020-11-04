# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, T, AB):
    import numpy as np
    arr = np.array(AB)
    bottom = arr.sum(axis=0)[-1]
    if bottom > T:
        print(-1)
        return
    sa = arr[:, 0] - arr[:, 1]
    sa = np.sort(sa).cumsum()
    sa = sa[sa <= T - bottom]
    print(N - sa.size)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, T = map(int, input().split())
    AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, T, AB)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
