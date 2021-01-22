# import sys
# sys.setrecursionlimit(10 ** 6)
# import bisect
# from collections import deque
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

# from decorator import stop_watch
#
#
# @stop_watch
def solve(K, A):
    A.reverse()

    if A[0] != 2:
        print(-1)
        return

    ans_min = A[0]
    ans_max = A[0] * 2 - 1
    for i in range(1, K):
        new_min = A[i] * (ceil(ans_min / A[i]))
        if ans_max < new_min:
            print(-1)
            return
        new_max = ans_max + (A[i] - ans_max % A[i]) - 1
        ans_min = new_min
        ans_max = new_max

    print(ans_min, ans_max)


if __name__ == '__main__':
    K = int(input())
    A = [int(i) for i in input().split()]
    solve(K, A)

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # solve()
