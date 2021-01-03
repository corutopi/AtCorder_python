# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, P):
    ans = 0
    n_map = [0] * (200000 + 1)
    for p in P:
        n_map[p] = 1
        while n_map[ans] == 1:
            ans += 1
        print(ans)


if __name__ == '__main__':
    N = int(input())
    P = [int(i) for i in input().split()]
    solve(N, P)

    # N = 3
    # P = [3, 2, 1, 0]
    # solve(N, P)

    # # test
    # from random import randint
    # from func import random_str
    # while True:
    #     N = 5
    #     P = [randint(0, N) for _ in range(N)]
    #     # P = [i + 1 for i in range(N)]
    #     solve(N, P)
