# import sys
# sys.setrecursionlimit(10 ** 6)
# # for pypy
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

# import bisect
# from collections import deque
# import string
from math import ceil, floor
inf = float('inf')
mod = 10 ** 9 + 7
mod2 = 998244353

"""
a <= b -> a <= b + EPS
a < b  -> a < b - EPS
a == b -> abs(a - b) < EPS
"""
EPS = 10 ** -7

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    A.sort(reverse=True)
    B = A[:3]
    ans = 0
    for i, j, k in ((i, j, k)
                    for i in range(3)
                    for j in range(3)
                    for k in range(3)):
        if i == j or j == k or k == i:
            continue
        ans = max(ans, int(str(B[i]) + str(B[j]) + str(B[k])))
    return ans


def solve_force(N, A):
    ans = 0
    for i, j, k in ((i, j, k)
                    for i in range(N)
                    for j in range(N)
                    for k in range(N)):
        if i == j or j == k or k == i:
            continue
        ans = max(ans, int(str(A[i]) + str(A[j]) + str(A[k])))
    return ans


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    print(solve(N, A))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # while True:
    #     N = 5
    #     A = random_ints(N, 1, 10)
    #     ans_a = solve(N, A)
    #     ans_b = solve_force(N, A)
    #     if ans_a != ans_b:
    #         print(N)
    #         print(A)
    #         print(ans_a)
    #         print(ans_b)
    #         break
