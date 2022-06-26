"""
解説AC
"""
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
def solve(N, X, Y, A):
    ans = ''
    if max(A) < X:
        ans = 'Second'
    elif X <= Y:
        ans = 'First' if sum(1 if a % (X + Y) >= X else 0 for a in A) > 0 \
            else 'Second'
    else:
        B = [a % (X + Y) for a in A]
        ans = 'Second' if all(b < X for b in B) or \
                          sum(1 if b - (X if b >= X else 0) >= Y else 0 for b in B) > 0 \
            else 'First'
    # print(ans)
    return ans


def solve_force(N, X, Y, A):
    ans = ''
    xy = [X, Y]

    def dfs(turn):
        if sum(0 if a < xy[turn] else 1 for a in A) == 0:
            return not turn
        re = turn
        for i in range(1, 4):
            flg = [0, 0]
            for j in range(2):
                if i >> j & 1 and A[j] >= xy[turn]:
                    flg[j] = 1
                    A[j] -= xy[turn]
            if sum(flg) > 0:
                tmp = dfs(not turn)
                for j in range(2):
                    A[j] += xy[turn] if flg[j] else 0
                if tmp == re:
                    return re
        return not re

    return 'Second' if dfs(0) else 'First'


if __name__ == '__main__':
    N, X, Y = map(int, input().split())
    A = [int(i) for i in input().split()]
    print(solve(N, X, Y, A))
    # print(solve_force(N, X, Y, A))

    # # test
    # from random import randint
    # import string
    # import tool.testcase as tt
    # from tool.testcase import random_str, random_ints
    # while True:
    #     N, X, Y = 2, randint(1, 10), randint(1, 10)
    #     A = [randint(1, 10), randint(1, 10)]
    #     a = solve(N, X, Y, A)
    #     b = solve_force(N, X, Y, A)
    #     if a != b:
    #         print(N, X, Y)
    #         print(A)
    #         print(a, b)
    #         break

