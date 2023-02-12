# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Z, W, a):
    if N == 1:
        print(abs(a[-1] - W))
    else:
        print(max(abs(a[-1] - W), abs(a[-2] - a[-1])))


if __name__ == '__main__':
    N, Z, W = map(int, input().split())
    a = [int(i) for i in input().split()]
    solve(N, Z, W, a)

    # # test
    # from random import randint
    # from func import random_str, random_ints
    # solve()
