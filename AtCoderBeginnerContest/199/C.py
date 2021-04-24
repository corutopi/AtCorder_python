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
def solve(N, S, Q, TAB):
    S = [S[i] for i in range(len(S))]
    # for t, a, b in TAB:
    #     if t == 1:
    #         S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
    #     else:
    #         S = S[N:] + S[:N]
    # print(''.join(S))
    chang_cnt = 0
    for t, a, b in TAB:
        if t == 1:
            if chang_cnt % 2 == 1:
                a += N if a <= N else -N
                b += N if b <= N else -N
            S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
        else:
            chang_cnt += 1
    S = S if chang_cnt % 2 == 0 else S[N:] + S[:N]
    print(''.join(S))


if __name__ == '__main__':
    # S = input()
    N = int(input())
    S = input()
    Q = int(input())
    TAB = [[int(i) for i in input().split()] for _ in range(Q)]
    # P = [int(input()) for _ in range(N)]
    solve(N, S, Q, TAB)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
