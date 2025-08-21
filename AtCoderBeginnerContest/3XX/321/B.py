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
def solve(N: int, X: int, A: list[int]):
    Asort = sorted(A)
    Xpre = sum(Asort[1:-1])
    needA = X - Xpre

    ans = 0
    if needA > Asort[-1]:
        ans = -1
    elif needA <= Asort[0]:
        ans = 0
    else:
        ans = needA

    print(ans)


if __name__ == '__main__':
    # S = input()
    # N = int(input())
    N, X = map(int, input().split())
    A = [int(i) for i in input().split()]
    # B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(N, X, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
