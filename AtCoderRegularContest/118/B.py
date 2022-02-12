# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from math import ceil, floor
from heapq import heappush, heappop

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(K, N, M, A):
    AM = [a * M for a in A]
    B = []
    B_sum = 0
    hq = []
    for i in range(K):
        B.append(AM[i] // N)
        heappush(hq, [B[-1] * N - AM[i], i])
        B_sum += B[-1]

    for _ in range(M - B_sum):
        _, now = heappop(hq)
        B[now] += 1

    print(*B)


if __name__ == '__main__':
    K, N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    solve(K, N, M, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # K, N, M = 10 ** 5, randint(1, 10 ** 9), randint(1, 10 ** 9)
    # A = []
    # m = N // K * 2
    # s = 0
    # for _ in range(K - 1):
    #     t = randint(0, m)
    #     t = t if s + t <= N else 0
    #     A.append(t)
    #     s += t
    # A.append(N - s)
    # solve(K, N, M, A)
