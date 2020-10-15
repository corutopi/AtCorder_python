# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, X):
    X_sort = sorted(X)
    xi = X_sort[N // 2 - 1]
    xj = X_sort[N // 2]
    for x in X:
        if x <= xi:
            print(xj)
        else:
            print(xi)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    X = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, X)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
