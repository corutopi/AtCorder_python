# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, Y):
    for i in range(0, N + 1):
        for j in range(0, N + 1 - i):
            k = N - i - j
            if i * 10000 + j * 5000 + k * 1000 == Y:
                print(i, j, k)
                return
    print(-1, -1, -1)


if __name__ == '__main__':
    N, Y = map(int, input().split())
    solve(N, Y)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
