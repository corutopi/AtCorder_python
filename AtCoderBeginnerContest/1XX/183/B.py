# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(Sx, Sy, Gx, Gy):
    if Sx > Gx:
        Sx, Sy, Gx, Gy = Gx, Gy, Sx, Sy
    l = abs(Gx - Sx)
    n = l * Sy / (Sy + Gy)
    print(Sx + n)


if __name__ == '__main__':
    Sx, Sy, Gx, Gy = map(int, input().split())
    solve(Sx, Sy, Gx, Gy)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
