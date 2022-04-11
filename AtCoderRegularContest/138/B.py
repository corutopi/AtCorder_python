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

# from decorator import stop_watch
#
#
# @stop_watch
def solve(N, A):
    if sum(A) == 0:
        return 'Yes'
    if A[0] == 1 or A[1] == 0:
        return 'No'
    revers_num = N - 1
    for i in range(1, N - 1):
        if A[i] == A[i + 1]:
            revers_num = i - 1
            break
    x = 0
    for i in range(revers_num + 1, N):
        if A[i - 1] != A[i]:
            x += 1
    if A[-1] == 0:
        x -= 1
    return 'Yes' if revers_num + 1 >= x else 'No'


def solve_force(N, A):
    def dfs(x):
        if len(x) == N:
            for i in range(N):
                if A[i] != x[i]:
                    return False
            return True
        return dfs([0] + [i ^ 1 for i in x]) or \
               dfs(x + [0])
    return 'Yes' if dfs([]) else 'No'


if __name__ == '__main__':
    N = int(input())
    A = [int(i) for i in input().split()]
    print(solve(N, A))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    #
    # print(solve(10, [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]))
    # print(solve_force(10, [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]))
    # while True:
    #     N = 10
    #     A = random_ints(N, 0, 1)
    #     if solve(N, A) != solve_force(N, A):
    #         print(*A)
    #         break
