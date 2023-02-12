# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    A = [0] + A + [0]
    sum_A = [0]
    for i in range(1, len(A)):
        sum_A.append(sum_A[-1] + abs(A[i] - A[i - 1]))
    for i in range(1, N + 1):
        print(sum_A[i - 1] +
              abs(A[i + 1] - A[i - 1]) +
              sum_A[-1] - sum_A[i + 1])


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    solve(N, A)

    # # test
    # from random import randint
    # from func import random_str
    # solve()
