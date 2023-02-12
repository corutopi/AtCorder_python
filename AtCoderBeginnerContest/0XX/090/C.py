# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M):
    if (N == 1) ^ (M == 1):
        print(max(N, M) - 2)
    else:
        print(N * M - (N * 2 + (M - 2) * 2))


if __name__ == '__main__':
    N, M = map(int, input().split())
    solve(N, M)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
