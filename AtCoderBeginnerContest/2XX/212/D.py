# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from heapq import *
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(Q, query):
    x2 = 0
    hq = []
    for q in query:
        if q[0] == 1:
            heappush(hq, q[1] - x2)
        elif q[0] == 2:
            x2 += q[1]
        elif q[0] == 3:
            print(heappop(hq) + x2)


if __name__ == '__main__':
    Q = int(input())
    query = [[int(i) for i in input().split()] for _ in range(Q)]
    solve(Q, query)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # Q = 2 * 10 ** 5
    # query = []
    # for _ in range(Q):
    #     q = int(random_str(1, '11111113'))
    #     if q == 1:
    #         query.append([1, randint(1, 10 ** 9)])
    #     elif q == 3:
    #         query.append([3])
    # solve(Q, query)
