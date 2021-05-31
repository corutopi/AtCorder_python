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
    A2 = [a ** 2 for a in A]
    sumA = [0]
    sumA2 = [0]
    for i in range(N):
        sumA.append(sumA[-1] + A[i])
        sumA2.append(sumA2[-1] + A2[i])
    ans = 0
    for i in range(N):
        ans += A2[i] * (N - i - 1) \
               + sumA2[-1] - sumA2[i + 1] \
               - 2 * A[i] * (sumA[-1] - sumA[i + 1])
    print(ans)


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
