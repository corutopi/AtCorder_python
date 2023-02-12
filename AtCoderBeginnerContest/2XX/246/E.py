# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
from collections import deque
# import string
from math import ceil, floor

inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A, B, S):
    ax, ay = A
    bx, by = B
    S = ['#' * (N + 2)] + ['#' + s + '#' for s in S] + ['#' * (N + 2)]
    board = [[inf] * (N + 2) for _ in range(N + 2)]
    board[ax][ay] = 0
    dq = deque([[ax, ay]])
    while dq:
        nx, ny = dq.popleft()
        nc = board[nx][ny]
        nextc = nc + 1
        d = 1
        while board[nx - d][ny + d] >= nextc and S[nx - d][ny + d] == '.':
            if board[nx - d][ny + d] == inf:
                board[nx - d][ny + d] = nextc
                dq.append([nx - d, ny + d])
            d += 1
        d = 1
        while board[nx + d][ny + d] >= nextc and S[nx + d][ny + d] == '.':
            if board[nx + d][ny + d] == inf:
                board[nx + d][ny + d] = nextc
                dq.append([nx + d, ny + d])
            d += 1
        d = 1
        while board[nx + d][ny - d] >= nextc and S[nx + d][ny - d] == '.':
            if board[nx + d][ny - d] == inf:
                board[nx + d][ny - d] = nextc
                dq.append([nx + d, ny - d])
            d += 1
        d = 1
        while board[nx - d][ny - d] >= nextc and S[nx - d][ny - d] == '.':
            if board[nx - d][ny - d] == inf:
                board[nx - d][ny - d] = nextc
                dq.append([nx - d, ny - d])
            d += 1

    print(board[bx][by] if board[bx][by] < inf else -1)


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    S = [input() for _ in range(N)]
    solve(N, A, B, S)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # N = 1500
    # A = random_ints(2, 1, N)
    # B = random_ints(2, 1, N)
    # while True:
    #     S = [random_str(N, '...#') for _ in range(N)]
    #     if S[A[0]][A[1]] == S[B[0]][B[1]] == '.': break
    # solve(N, A, B, S)
