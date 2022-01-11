# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
# import string
from heapq import heappush, heappop
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, K, P):
    hq = P[:K]
    hq.sort()
    print(hq[0])
    for i in range(K, N):
        if hq[0] < P[i]:
            heappop(hq)
            heappush(hq, P[i])
        print(hq[0])

if __name__ == '__main__':
    N, K = map(int, input().split())
    P = [int(i) for i in input().split()]
    solve(N, K, P)

    # # test
    # from random import randint, shuffle
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N, K = 5 * 10 ** 5, 5 * 10 ** 5 // 2
    # P = [i + 1 for i in range(N)]
    # shuffle(P)
    # solve(N, K, P)
