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
def solve(N, A):
    ans = []
    for i in range(N):
        if i == N - 1:
            ans.append(A[i])
        elif A[i] == A[i + 1]:
            ans.append(A[i])
        elif A[i] > A[i + 1]:
            for j in range(A[i] - A[i + 1]):
                ans.append(A[i] - j)
        elif A[i] < A[i + 1]:
            for j in range(A[i + 1] - A[i]):
                ans.append(A[i] + j)
    print(*ans)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
