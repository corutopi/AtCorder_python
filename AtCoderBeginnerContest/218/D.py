# 解説を参考に作成
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
def solve(N, S, T):
    if sum(1 for i in range(N) for j in range(N) if S[i][j] == '#') != \
            sum(1 for i in range(N) for j in range(N) if T[i][j] == '#'):
        print('No')
        return

    for _ in range(4):
        for i, j in ((i, j) for i in range(N) for j in range(N)):
            if S[i][j] == '#':
                Si, Sj = i, j
                break

        for i, j in ((i, j) for i in range(N) for j in range(N)):
            if T[i][j] == '#':
                Ti, Tj = i, j
                break

        offset_i = Ti - Si
        offset_j = Tj - Sj

        for i, j in ((i, j) for i in range(N) for j in range(N)):
            if 0 <= i + offset_i < N and 0 <= j + offset_j < N:
                if S[i][j] != T[i + offset_i][j + offset_j]:
                    break
            else:
                if S[i][j] == '#':
                    break
        else:
            print('Yes')
            return

        S = list(zip(*S[::-1]))

    print('No')


if __name__ == '__main__':
    # S = input()
    N = int(input())
    S = [input() for _ in range(N)]
    T = [input() for _ in range(N)]
    solve(N, S, T)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
