# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(S, T):
    if S == 'Y':
        print(T.upper())
    else:
        print(T)


if __name__ == '__main__':
    S = input()
    T = input()
    # N = int(input())
    # N, M = map(int, input().split())
    # A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(S, T)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
