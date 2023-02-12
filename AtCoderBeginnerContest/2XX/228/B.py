# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, X, A):
    friend = [0] * (N + 1)
    A = [0] + A
    x = X
    friend[x] = 1
    while friend[A[x]] == 0:
        x = A[x]
        friend[x] = 1
    print(sum(friend))


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, X = map(int, input().split())
    A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(N, X, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
