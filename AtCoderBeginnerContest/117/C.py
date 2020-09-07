# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, M, Xi):
    lengthes = []
    Xi.sort()
    for i in range(1, M):
        lengthes.append(abs(Xi[i - 1] - Xi[i]))
    lengthes.sort()
    num = N if N < M else M
    print(sum(lengthes[:M - num]))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, M = map(int, input().split())
    Xi = [int(i) for i in input().split()]
    # Bi = [int(i) for i in input().split()]
    # ABi = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, M, Xi)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
