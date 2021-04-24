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
def solve(N, A, B):
    max_A = max(A)
    min_B = min(B)
    print(min_B - max_A + 1 if min_B >= max_A else 0)


if __name__ == '__main__':
    # S = input()
    N = int(input())
    # N, M = map(int, input().split())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    # AB = [[int(i) for i in input().split()] for _ in range(N)]
    # P = [int(input()) for _ in range(N)]
    solve(N, A, B)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
