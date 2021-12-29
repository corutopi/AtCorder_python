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
def solve(N, A):
    sorted_A = sorted(A)
    dict_A = {sorted_A[i]: i % 2 for i in range(N)}
    print(sum([0 if dict_A[A[i]] == i % 2 else 1 for i in range(N)]) // 2)


if __name__ == '__main__':
    N = int(input())
    A = [int(input()) for _ in range(N)]
    solve(N, A)

    # # test
    # from random import randint, shuffle
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # N = 5
    # A = [i for i in range(1, N + 1)]
    # shuffle(A)
    # print(A)
    # solve(N, A)
