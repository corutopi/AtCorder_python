# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
from heapq import heappush, heappop
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353


# from decorator import stop_watch
#
#
# @stop_watch
def solve(R, C, A, B):
    LEFT, RIGHT, UP, DOWN = 0, 1, 2, 3
    cost = [[inf] * C for _ in range(R)]
    cost[0][0] = 0
    visited = [[0] * C for _ in range(R)]
    queue = [[] for _ in range((R + C) * max(max([max(a) for a in A]),
                                             max([max(b) for b in B]),
                                             1))]
    queue[0].append([0, 0])
    for c in range(len(queue)):
        for i, j in queue[c]:
            if visited[i][j] == 1: continue
            visited[i][j] = 1
            # left
            if j - 1 >= 0:
                tr, tc = i, j - 1
                if c + A[tr][tc] < cost[tr][tc]:
                    cost[tr][tc] = c + A[tr][tc]
                    queue[cost[tr][tc]].append([tr, tc])
            # right
            if j + 1 < C:
                tr, tc = i, j + 1
                if c + A[tr][tc - 1] < cost[tr][tc]:
                    cost[tr][tc] = c + A[tr][tc - 1]
                    queue[cost[tr][tc]].append([tr, tc])
            # up
            if i + 1 < R:
                tr, tc = i + 1, j
                if c + B[tr - 1][tc] < cost[tr][tc]:
                    cost[tr][tc] = c + B[tr - 1][tc]
                    queue[cost[tr][tc]].append([tr, tc])
            # down
            tc = j
            for x in range(1, i + 1):
                tr = i - x
                if c + (1 + x) < cost[tr][tc]:
                    cost[tr][tc] = c + (1 + x)
                    queue[cost[tr][tc]].append([tr, tc])
    print(cost[-1][-1])


if __name__ == '__main__':
    R, C = map(int, input().split())
    A = [[int(i) for i in input().split()] for _ in range(R)]
    B = [[int(i) for i in input().split()] for _ in range(R - 1)]
    solve(R, C, A, B)

    # # test
    # from random import randint
    #
    # # import string
    # # import tool.testcase as tt
    # # from tool.testcase import random_str, random_ints
    #
    # while True:
    #     R, C = 500, 500
    #     A = [[randint(0, 0) for _ in range(C - 1)] for _ in range(R)]
    #     B = [[randint(0, 0) for _ in range(C)] for _ in range(R - 1)]
    #     # A = [random_ints(C - 1, 0, 1000) for _ in range(R)]
    #     # B = [random_ints(C, 0, 1000) for _ in range(R - 1)]
    #     solve(R, C, A, B)
