# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
from collections import deque
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
def solve(Q, query):
    dq = deque([])
    sorted = []
    for q in query:
        if q[0] == 1:
            dq.append(q[1])
        elif q[0] == 2:
            if sorted:
                print(heappop(sorted))
            else:
                print(dq.popleft())
        elif q[0] == 3:
            while dq:
                heappush(sorted, dq.popleft())


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
    #     i = int(random_str(1, '111111111111123333'))
    #     if i == 1:
    #         query.append([i, randint(0, 10 ** 9)])
    #     else:
    #         query.append([i])
    # solve(Q, query)
