# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, TXY):
    now_x, now_y, now_t = 0, 0, 0
    for t, x, y in TXY:
        tt = t - now_t
        load = abs(x - now_x) + abs(y - now_y)
        if not(tt >= load and (tt - load) % 2 == 0):
            print('No')
            return
        now_x, now_y = x, y
        now_t = t
    print('Yes')


if __name__ == '__main__':
    N = int(input())
    TXY = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, TXY)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
