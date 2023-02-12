# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    for i in range(N):
        A[i] -= i + 1
    A.sort()
    center = A[N // 2]
    print(sum([abs(a - center) for a in A]))


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
