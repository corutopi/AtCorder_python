# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N):
    mod = 10 ** 9 + 7
    a = 10 ** N - (9 ** N + 9 ** N - 8 ** N)
    print(a % mod)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    # Ai = [int(i) for i in input().split()]
    # Bi = [int(i) for i in input().split()]
    # ABi = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
